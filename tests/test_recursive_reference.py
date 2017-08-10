from mongoengine import Document, fields, connect
import unittest


class MyDocument(Document):
    parent = fields.ReferenceField("MyDocument")


class SimpleDocumentTest(unittest.TestCase):

    def test_document(self):
        MyDocument()


class MoreComplexRecursiveDocument(unittest.TestCase):

    def test_import(self):
        connect('test', host='mongomock://test')
        from .fixtures.recursive_definition import UserForm
        UserForm()
