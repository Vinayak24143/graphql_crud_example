from graphene_django.types import DjangoObjectType
from book.models import Book, Writer
import graphene
from graphql import GraphQLError


class BookType(DjangoObjectType):
    class Meta:
        model=Book
        fields=['id','name','writer']


class BookUpdateMutation(graphene.Mutation):
    class Arguments:
        name=graphene.String(required=True)
        id = graphene.ID()
        writer = graphene.String()
    book=graphene.Field(BookType)

    @classmethod
    def mutate(cls,root,info,name,id,writer):
        try:
            writer_ins=Writer.objects.get(name=writer)
        except Writer.DoesNotExist:
            raise GraphQLError('Invalid writer')
        book=Book.objects.get(pk=id)
        book.name=name
        book.writer=writer_ins
        book.save()
        return BookUpdateMutation(book=book)


class BookCreateMutation(graphene.Mutation):
    class Arguments:
        name=graphene.String(required=True)
        writer = graphene.String()
    book=graphene.Field(BookType)

    @classmethod
    def mutate(cls,root,info,name,writer):
        try:
            writer_ins=Writer.objects.get(name=writer)
        except Writer.DoesNotExist:
            raise GraphQLError('Invalid writer')
        book=Book(name=name,writer=writer_ins)
        book.save()
        return BookUpdateMutation(book=book)

class BookDeleteMutation(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
    book=graphene.Field(BookType)

    @classmethod
    def mutate(cls,root,info,id):

        book=Book.objects.get(pk=id)
        book.delete()
        return BookUpdateMutation(book=book)