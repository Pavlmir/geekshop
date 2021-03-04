from django.urls import re_path

from mainapp.views import products

app_name = 'mainapp'

urlpatterns = [
    re_path(r"^$", products, name='index'),
    re_path(r"^product/(?P<category_id>\d+)/$", products, name='product'),
    re_path(r"^page/(?P<page>\d+)/$", products, name='page')
]
