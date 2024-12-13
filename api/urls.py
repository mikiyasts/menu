
from django.urls import path

from . import views
urlpatterns =[
    path('endpoints/',views.api_endpoints,),
    path('restaurant-list/',views.restaurant_list),
    path('restaurant-detail/<str:pk>/',views.restaurant_deatil_list)
]