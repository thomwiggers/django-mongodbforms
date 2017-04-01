from mongoengine import Document, fields
import unittest


class MyDocument(Document):
    parent = fields.ReferenceField("MyDocument")


class SimpleDocumentTest(unittest.TestCase):

    def test_document(self):
        MyDocument()

