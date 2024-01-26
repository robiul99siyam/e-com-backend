from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path,include



#-------------- rotuer all -------------------->
routers = DefaultRouter()
routers.register('Featuere_list', views.Feature_productViewset)
routers.register('new_arreval_list', views.New_arrevalViewset)

urlpatterns = [
    path('', include(routers.urls)),
    path('', include(routers.urls)),
]
