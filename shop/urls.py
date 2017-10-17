from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
]