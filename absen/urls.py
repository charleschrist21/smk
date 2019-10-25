from rest_framework.urlpatterns import format_suffix_patterns
from .api.views import tanggalAbsenCreate,tanggalAbsenDetailAndEdit,bulanAbsenCreate,bulanAbsenCreateDetailAndEdit
from django.conf.urls import url

urlpatterns={
    url(r'^absen/tanggal/$', tanggalAbsenCreate.as_view(),name='tanggalAbsen'),
    url(r'^absen/tanggal/edit/(?P<pk>[0-9+])/$', tanggalAbsenDetailAndEdit.as_view(),name='tanggalAbsenEdit'),
    url(r'^absen/bulan/$', bulanAbsenCreate.as_view(),name='bulanAbsen'),
    url(r'^absen/bulan/edit/(?P<pk>[0-9+])/$', tanggalAbsenDetailAndEdit.as_view(),name='bulanAbsenEdit'),

}


urlpatterns = format_suffix_patterns(urlpatterns)