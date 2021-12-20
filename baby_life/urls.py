from django.urls import re_path
from .views import baby_eat
from .views import baby_sleep
from .views import baby_not_sleep
from django.urls import path


urlpatterns = [
    path('eat', baby_eat, name='eat'),
    path('not_sleep', baby_not_sleep, name='not_sleep'),
    path('sleep', baby_sleep, name='sleep'),
]
