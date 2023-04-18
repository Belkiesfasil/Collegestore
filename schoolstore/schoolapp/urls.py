
from django.urls import path
from . import views
app_name='schoolapp'
urlpatterns = [


    # path('',views.home,name='home'),
    path('',views.allStream,name='allStream'),
    path('<slug:c_slug>/',views.allStream,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodDetail, name='prodCatdetail')






]