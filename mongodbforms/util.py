from collections import defaultdict

from django.conf import settings
from django.utils.module_loading import import_string as import_by_path

from .documentoptions import DocumentMetaWrapper, LazyDocumentMetaWrapper
from .fieldgenerator import MongoDefaultFormFieldGenerator


def load_field_generator():
    if hasattr(settings, 'MONGODBFORMS_FIELDGENERATOR'):
        return import_by_path(settings.MONGODBFORMS_FIELDGENERATOR)
    return MongoDefaultFormFieldGenerator


def init_document_options(document):
    if not isinstance(document._meta,
                      (DocumentMetaWrapper, LazyDocumentMetaWrapper)):
        document._meta = DocumentMetaWrapper(document)
    # Workaround for Django 1.7+
    document._deferred = False  # This means we've got all values

    def serializable_value(self, field_name):
        # FIXME: Wrong implementation for Relations
        # (https://github.com/django/django/blob/master/django/db/models/base.py#L601)
        return self._meta.get_field(field_name)
    document.serializable_value = serializable_value

    return document


def get_document_options(document):
    return DocumentMetaWrapper(document)


def format_mongo_validation_errors(validation_exception):
    """Returns a string listing all errors within a document"""

    def generate_key(value, prefix=''):
        if isinstance(value, list):
            value = ' '.join([generate_key(k) for k in value])
        if isinstance(value, dict):
            value = ' '.join([
                generate_key(v, k) for k, v in value.items()
            ])

        results = "%s.%s" % (prefix, value) if prefix else value
        return results

    error_dict = defaultdict(list)
    for k, v in validation_exception.to_dict().items():
        error_dict[generate_key(v)].append(k)
    return ["%s: %s" % (k, v) for k, v in error_dict.items()]


# Taken from six (https://pypi.python.org/pypi/six)
# by "Benjamin Peterson <benjamin@python.org>"
#
# Copyright (c) 2010-2013 Benjamin Peterson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""
    return meta("NewBase", bases, {})
