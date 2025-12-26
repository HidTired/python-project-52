from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db import models
from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task

User = get_user_model()

class LabelListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'label/label_list.html'

class LabelCreateView(LoginRequiredMixin, CreateView):
    model = Label
    fields = ['name']
    success_url = reverse_lazy('labels:list')
    template_name = 'general/general_form.html'

class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    success_url = reverse_lazy('labels:list')
    template_name = 'general/general_delete_confirm.html'

class StatusListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'status/status_list.html'

class StatusCreateView(LoginRequiredMixin, CreateView):
    model = Status
    fields = ['name']
    success_url = '/'
    template_name = 'general/general_form.html'

class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    fields = ['name']
    success_url = '/'
    template_name = 'general/general_form.html'

class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    success_url = '/'
    template_name = 'general/general_delete_confirm.html'

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'

class UserCreateView(LoginRequiredMixin,  CreateView):
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password')
    template_name = 'general/general_form.html'
    success_url = '/'

class UserUpdateView(LoginRequiredMixin,  UpdateView):
    model = User
    fields = ('username', 'first_name', 'last_name', 'email')
    template_name = 'general/general_form.html'
    success_url = '/'

class UserDeleteView(LoginRequiredMixin,  DeleteView):
    model = User
    success_url = '/'
    template_name = 'general/general_delete_confirm.html'

def test_func(self):
    return self.request.user.is_superuser
class UserPassesTestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class UserCreateView(LoginRequiredMixin,  CreateView):
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password')
    template_name = 'general/general_form.html'
    success_url = '/'
class UserPassesTestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser
class UserCreateView(LoginRequiredMixin, CreateView):
    model = get_user_model()
    fields = ('username', 'first_name', 'last_name', 'email', 'password')
    template_name = 'general/general_form.html'
    success_url = '/'
