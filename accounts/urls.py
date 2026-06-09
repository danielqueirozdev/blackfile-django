from . import views
from django.urls import path


app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('register/created', views.register_create_view, name='register_create'),
    path('login/', views.login_view, name='login'),
    path('login/created', views.login_create_view, name='login_create'),
    path('logout/', views.logout_view, name='logout'),
]