from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('info/', InfoPageView.as_view(), name='info'),
]