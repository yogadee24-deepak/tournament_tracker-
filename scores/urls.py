from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Authentication URLs
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='scores/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    # CRUD URLs
    path('', views.match_list, name='match_list'),                   # Read All
    path('match/add/', views.add_match, name='add_match'),           # Create
    path('match/edit/<int:match_id>/', views.edit_match, name='edit_match'), # Update
    path('match/delete/<int:match_id>/', views.delete_match, name='delete_match'), # Delete
]