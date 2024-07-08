from django.urls import path
from salary import views
from salary.views import *

urlpatterns = [
path('', views.home, name='home'),
path('addemployee', views.addemployee, name='addemployee'),

]