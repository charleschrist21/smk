"""AbsenSchool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
from absen.api import views as absen_views

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^sekolah/siswa/',include('siswa.urls')),
    url(r'^sekolah/siswa/absen/tanggal/$', absen_views.tanggalAbsenCreate.as_view(), name='absensiswacreate'),
    url(r'^sekolah/siswa/absen/tanggal/detail/(?P<pk>[0-9+])/$', absen_views.tanggalAbsenDetailAndEdit.as_view(), name='siswatanggalabsen'),
    url(r'^sekolah/siswa/absen/bulan/$', absen_views.bulanAbsenCreate.as_view(), name='absenbulancreate'),
    url(r'^sekolah/siswa/absen/bulan/detail/(?P<pk>[0-9+])/$', absen_views.bulanAbsenCreateDetailAndEdit.as_view(), name='siswabulanabsen'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
