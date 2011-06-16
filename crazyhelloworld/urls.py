from django.conf.urls.defaults import *
from helloworld.views import hello
 
urlpatterns = patterns('',
	('^hello/$', hello),
)
