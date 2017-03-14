from django.conf.urls import url
from . import views

app_name = "xmlToServer"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^checkpatients/', views.checkpatients, name='checkpatients'),
    url(r'^transfer/', views.transfer, name='transfer')
]