from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .api.views import tagihanCreate,tagihanDetailAndEdit

urlpatterns={
    url(r'^tagihan/$', tagihanCreate.as_view(), name='tagihanCreate'),
    url(r'^tagihan/edit/(?P<pk>[0-9+])/$', tagihanDetailAndEdit.as_view(), name='taguhanedit')
}

urlpatterns = format_suffix_patterns(urlpatterns)