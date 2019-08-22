from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .api.views import GuruCreate,guruDetailAndEdit

urlpatterns={
    url(r'^$', GuruCreate.as_view(), name='gurucreate'),
    url(r'^detail/(?P<pk>[0-9+])/$', guruDetailAndEdit.as_view(), name='gurudetail')
}

urlpatterns = format_suffix_patterns(urlpatterns)