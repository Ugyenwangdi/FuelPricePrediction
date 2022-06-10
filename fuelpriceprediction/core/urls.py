from django.urls import path
from .views import home, predict, dashboard, bar, pie, line, box
from core.dash_apps.finished_apps import simpleexample, barchart, piechart, linechart, boxplot
app_name = 'core'

urlpatterns = [
    path('',home,name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('bar/', bar, name='bar'),
    
    path('pie/', pie, name='pie'),
    path('line/', line, name='line'),
    path('other/', box, name='other'),
    
    
    path('predict/', predict, name='predict'),
]