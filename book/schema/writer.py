from graphene_django.types import DjangoObjectType
from book.models import Writer
import graphene

class WriterType(DjangoObjectType):
    class Meta:
        model=Writer
        fields=['id','name']



class WriterUpdateMutation(graphene.Mutation):
    class Arguments:
        name=graphene.String(required=True)
        id = graphene.ID()
    writer=graphene.Field(WriterType)

    @classmethod
    def mutate(cls,root,info,name,id):
        writer=Writer.objects.get(pk=id)
        writer.name=name
        writer.save()
        return WriterUpdateMutation(writer=writer)

class WriterCreateMutation(graphene.Mutation):
    class Arguments:
        name=graphene.String(required=True)
    writer=graphene.Field(WriterType)

    @classmethod
    def mutate(cls,root,info,name):
        writer=Writer(name=name)
        writer.name=name
        writer.save()
        return WriterUpdateMutation(writer=writer)

class WriterDeleteMutation(graphene.Mutation):
    class Arguments:
        id=graphene.ID(required=True)
    writer=graphene.Field(WriterType)

    @classmethod
    def mutate(cls,root,info,id):
        writer=Writer.objects.get(id=id)
        writer.delete()
        return WriterUpdateMutation(writer=writer)