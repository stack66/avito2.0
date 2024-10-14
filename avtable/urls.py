from django.urls import path
from . import views

urlpatterns = [
    #path('', views.articles, name='articles'),
    path('', views.home, name='home'),
    path('flat/<str:id>/', views.obj_detail, name='flat'),
    path('house/<int:id>/', views.obj_detail, name='house'),
    path('search/', views.search, name='search'),
    path('find/', views.find_st, name='find'),
]