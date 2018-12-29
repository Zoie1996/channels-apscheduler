from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.data, name='data'),
    path(r'data', views.showdata, name='data'),
]
