Django dummy user
============

*Django-faker* uses `fake-factory`_ package to generate test data for Django models and templates.

|pypi| |unix_build| |windows_build| |coverage| |downloads| |license|

How to use
----------

To install Django-faker you can use pip::

    pip install django-dummy-user==0.1


Configuration
~~~~~~~~~~~~~

In django application `settings.py`::

    INSTALLED_APPS = (

        # ...
        'dummy-user',
    )



Running the package
-----------------

Generate user 

    $ python manage.py create_user <int:total>

Delete all user

    $ python manage.py delete_all_users



- Add requirements
- Fake browser preview

0.1 - 01-December-2012
----------------------

- Add django Model instance generator
- Add django template tag and filter


Source: https://www.github.com/joke2k/faker/

