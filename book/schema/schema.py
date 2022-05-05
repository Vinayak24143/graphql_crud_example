import graphene
from book.models import Book, Writer
from .book import BookType, BookCreateMutation,BookDeleteMutation,BookUpdateMutation
from .writer import WriterType, WriterUpdateMutation, WriterDeleteMutation, WriterCreateMutation


class Query(graphene.ObjectType):
    all_books=graphene.List(BookType)
    writer_by_name=graphene.Field(WriterType, name=graphene.String(required=True))

    def resolve_all_books(root,info,**kwargs):
        return Book.objects.select_related('writer').all()

    def resolve_writer_by_name(root,info,name):
        try:
            return Writer.objects.get(name=name)
        except Writer.DoesNotExist:
            return None


class Mutation(graphene.ObjectType):
    update_writer=WriterUpdateMutation.Field()
    create_writer=WriterCreateMutation.Field()
    delete_writer=WriterDeleteMutation.Field()
    update_book = BookUpdateMutation.Field()
    create_book = BookCreateMutation.Field()
    delete_book = BookDeleteMutation.Field()
    


schema = graphene.Schema(query=Query,mutation=Mutation)