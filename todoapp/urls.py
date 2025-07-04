from django.urls import path
from .import views

urlpatterns=[
    path('', views.home, name='home-page'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  
    path('delete/<int:id>/', views.delete, name='delete'),

    path('update/<int:id>/', views.update, name='update'),

]