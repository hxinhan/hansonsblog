import sae

from blog import wsgi

application = sae.create_wsgi_app(wsgi.application)
