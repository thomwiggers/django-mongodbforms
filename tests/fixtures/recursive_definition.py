# Author: @lucashowell in
# https://github.com/thomwiggers/django-mongoengine-forms/issues/10#issuecomment-321387694
from mongoengine import Document
from mongoengine import StringField, ReferenceField

from mongodbforms import DocumentForm


class Group(Document):
    name = StringField(required=True, unique=True)
    parent_group = ReferenceField("Group")


class User(Document):
    name = StringField(required=True, unique=True)
    default_group = ReferenceField("Group")


class UserForm(DocumentForm):
    class Meta:
        document = User
        fields = ["name", "default_group", ]
