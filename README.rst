Django dummy user
============

Django generate data dummy user 


How to use
----------

To install django-dummy-user you can use pip::

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


Source: https://github.com/keselyoleren/django-dummy-user/

