from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/$', views.UserListView.as_view(), name='users'),
    url(r'^user/(?P<pk>\d+)$', views.UserDetailView.as_view(), name='user-detail'),
]