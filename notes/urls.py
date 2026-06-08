import views
from django.urls import path

app_name = 'notes'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('note/<int:id>/', views.note, name='note'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
]