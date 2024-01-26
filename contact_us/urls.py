from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path,include

#--------------------- Router views ------------------>
router = DefaultRouter()
router.register('contact_us', views.ContactViewSet)
urlpatterns = [
    path('',include(router.urls)),
]

