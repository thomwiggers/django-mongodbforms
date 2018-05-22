Changelog
=========

Version 0.4.6
-------------
* Hold a lazy queryset reference to prevent early database access (PR #15 by @terencehonles)

Version 0.4.5
-------------
* Lazy load field generator in documents package (PR #14)
* Cover bare excepts
* Fix tests on Python 3
* Limit to Django<2 if installing on Python >=3.5

Version 0.4.4
-------------
* Try to fix a max recursion depth issue (#10)

Version 0.4.3
-------------

* Bug: fix 'Field assigned before declaration' error (PR #8)
* Fix MongoEngine 0.11.0 compatibility by importing errors from `mongoengine.errors` (#9)

Version 0.4.2
-------------

* Bug: Can't customise widget. (PR #6)
* Bug: `BaseDocumentForm` should instantiate new document if `instance=None` (PR #7)

Version 0.4.1
-------------

* Added Changelog
* Use `check_call` instead of `call` in `setup.py` (PR #2)
* Fix typo caused by pep8 cleanup (PR #3)

Version 0.4.0
-------------

* Initial fork release
* Compatibility with Django 1.9
* Removed some dead code
