from django.urls import re_path

from adminapp import views

app_name = 'adminapp'

urlpatterns = [
    re_path(r"^$", views.index, name='index'),
    re_path(r"^admin-users-read/$", views.UserListView.as_view(), name='admin_users_read'),
    re_path(r"^admin-users-create/$", views.UserCreateView.as_view(), name='admin_users_create'),
    re_path(r"^admin-users-update/(?P<pk>\d+)/$", views.UserUpdateView.as_view(), name='admin_users_update'),
    re_path(r"^admin-users-delete/(?P<pk>\d+)/$", views.UserDeleteView.as_view(), name='admin_users_delete'),
]
