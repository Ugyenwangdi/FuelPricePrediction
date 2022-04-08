from django.urls import path
from .views import index, predict

app_name = 'core'

urlpatterns = [
    path('',index,name='index'),
    path('predict/', predict, name='predict'),
]