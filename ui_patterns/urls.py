from django.conf.urls.defaults import *
from .views import *

urlpatterns = patterns('',

  url(r'^group/(?P<category>.*)/$', PatternCategoryView.as_view(), name="category"),
  url(r'^(?P<slug>.*)/$', PatternDetailView.as_view(), name="detail"),
  url(r'^$', IndexView.as_view(), name="index"),
)
