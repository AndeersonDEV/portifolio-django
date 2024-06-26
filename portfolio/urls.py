from django.urls import path
from portfolio.views import index
from portfolio.views import about

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about')
]