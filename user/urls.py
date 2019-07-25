from django.conf.urls import url,include
from rest_framework import routers
from .api.views import userViewSet

routers = routers.DefaultRouter()
routers.register(r'users', userViewSet)

urlpatterns =[
    url(r'^', include(routers.urls)),
    url(r'^auth/', include('rest_auth.urls'))
]