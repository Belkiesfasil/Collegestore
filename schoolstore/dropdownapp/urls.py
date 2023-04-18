from django.urls import path
from . import views

app_name='dropdownapp'

urlpatterns = [
    path('', views.getdata, name="getdata"),
]

