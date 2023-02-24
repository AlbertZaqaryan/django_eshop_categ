from django.urls import path
from . import views

urlpatterns=[
    path('', views.HomeListView.as_view(), name='home'),
    path('shop/<int:id>/', views.ShopListView.as_view(), name='shop'),
]