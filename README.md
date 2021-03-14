# Simple SSO Login Form

1. pip install -r requirments
2. python manage.py migrate
3. python manage.py runserver
4. Go to Django admin and add a new Application with the following configuration:
   - ``client_id`` and ``client_secret`` should be left unchanged
   - ``user`` should be your superuser
   - ``redirect_uris`` should be left blank
   - ``client_type`` should be set to ``confidential``
   - ``authorization_grant_type`` should be set to ``'Resource owner password-based'``
   - ``name`` can be set to whatever you'd like
5. create token in github and running following command::

    `curl -X POST -d "grant_type=convert_token&client_id=<django-oauth-generated-client_id>&client_secret=<django-oauth-generated-client_secret>&backend=github&token=<github_token>" http://127.0.0.1:8000/auth/convert-token`
6. This request returns an "access_token" that you should use with every HTTP requests to your REST API::

    `curl -H "Authorization: Bearer <backend_name> <backend_token>" http://127.0.0.1:8000/route/to/your/view `
