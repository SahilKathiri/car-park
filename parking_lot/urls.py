from django.conf.urls import include, url

from . import views

app_name = 'parking_lot'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
