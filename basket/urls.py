from django.urls import re_path

from basket.views import basket_add, basket_remove, basket_edit

app_name = 'basket'

urlpatterns = [
    re_path(r"^basket-add/(?P<product_id>\d+)/$", basket_add, name='basket_add'),
    re_path(r"^basket-remove/(?P<id>\d+)/$", basket_remove, name='basket_remove'),
    re_path(r"^edit/(?P<id>\d+)/(?P<quantity>\d+)/$", basket_edit, name='basket_edit'),
]