from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from .api.views import siswaCreate,siswaDetailAndEdit


urlpatterns={
    url(r'^$', siswaCreate.as_view(), name='siswacreate'),
    url(r'^detail/(?P<pk>[0-9+])/$',siswaDetailAndEdit.as_view(), name='siswadetail'),
   
}
urlpatterns = format_suffix_patterns(urlpatterns)