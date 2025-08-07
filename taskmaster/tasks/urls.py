from django.urls import path
from . import views

# URL patterns for the task management application
urlpatterns = [
    # Root URL - displays the list of tasks
    path('', views.task_list, name='task_list'),
    
    # URL for viewing a specific task's details
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    
    # URL for creating a new task
    path('task/new/', views.task_create, name='task_create'),
    
    # URL for editing an existing task
    path('task/<int:pk>/edit/', views.task_update, name='task_update'),
    
    # URL for deleting a task
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    
    # URL for user registration
    path('register/', views.register_view, name='register'),
    
    # URL for user login
    path('login/', views.login_view, name='login'),
    
    # URL for user logout
    path('logout/', views.logout_view, name='logout'),
]