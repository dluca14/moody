=====
Polls
=====
**Moody** is a Django project which collects multiple selfies
and returns info based on them and user locations

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "moody" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'moody',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('moody/', include('moody.urls')),

3. Run ``python manage.py migrate`` to create the moody models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a user (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/moods/ to participate in the poll.