from genart.settings import *

import django_heroku

Debug = False

django_heroku.settings(locals())
