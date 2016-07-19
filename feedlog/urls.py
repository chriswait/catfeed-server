from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add_feed$', views.add_feed, name="add_feed"),
    url(r'^feeds$', views.feeds, name="block"),
]
