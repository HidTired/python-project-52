from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from task_manager.views import (
    UserCreateView,
    UserDeleteView,
    UserListView,
    UserUpdateView,
)

app_name = 'users'

urlpatterns = [
    path('', UserListView.as_view(), name='list'),
    path('create/', UserCreateView.as_view(), name='create'), 
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update'), 
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete'), 
    path('login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]