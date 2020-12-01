from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^(?P<p_name>[^0-9]+)/$', views.frise, name='frise')
]
