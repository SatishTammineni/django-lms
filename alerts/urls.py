from django.conf.urls.defaults import *
from alerts.views import AlertList
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('alerts.views',
                       url('^$', login_required(AlertList.as_view()), name = 'list'),
                       )
