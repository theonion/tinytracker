===========
TinyTracker
===========

TinyTracker is a tiny gevent-based wsgi application, designed to be run with uwsgi,
and to periodically send tracking data to a carbon endpoint.

Try it out like this::

    > uwsgi --http 127.0.0.1:3333 \
            --module tinytracker.wsgi:application \
            --master --gevent 100
