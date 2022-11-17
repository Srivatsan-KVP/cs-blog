from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('blog/', views.Blog),
    path('blog/<str:uid>/', views.Blog_Post),
    path('auth/', views.Auth),
    path('logout/', views.Logout)
]