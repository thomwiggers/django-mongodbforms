from mongoengine import Document, fields
from mongodbforms import DocumentForm
import unittest


class MyDocument(Document):
    mystring = fields.StringField()
    myverbosestring = fields.StringField(verbose_name="Foobar")
    myrequiredstring = fields.StringField(required=True)


class MyForm(DocumentForm):
    class Meta:
        document = MyDocument


class SimpleDocumentTest(unittest.TestCase):

    def test_form(self):
        form = MyForm()
        self.assertEquals(len(form.fields), 3)
        self.assertFalse(form.fields['mystring'].required)
        self.assertEquals(form.fields['myverbosestring'].label, "Foobar")
        self.assertTrue(form.fields['myrequiredstring'].required)
