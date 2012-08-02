
from django.conf.urls.defaults import *


urlpatterns = patterns('',
            (r'^$', 'img_viewer.views.base'),
            (r'^contact', 'img_viewer.views.contact'),
            (r'^imgview', 'img_viewer.views.imgview')

)

