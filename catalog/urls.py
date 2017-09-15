from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    # url(r'^$', views.Index, name='index'),
    # url(r'^$', views.Index, name='index'),
]