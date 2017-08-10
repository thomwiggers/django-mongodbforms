from mongoengine import Document, fields
import unittest


class MyDocument(Document):
    parent = fields.ReferenceField("MyDocument")


class SimpleDocumentTest(unittest.TestCase):

    def test_document(self):
        MyDocument()


class MoreComplexRecursiveDocument(unittest.TestCase):

    def test_import(self):
        from .fixtures.recursive_definition import UserForm
        UserForm()
