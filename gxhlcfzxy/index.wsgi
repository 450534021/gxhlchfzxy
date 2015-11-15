import sae
from photo import wsgi


application = sae.create_wsgi_app(wsgi.application)