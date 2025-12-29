from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.labels.models import Label
from task_manager.statuses.models import Status

User = get_user_model()


GENERAL_FORM_TEMPLATE = 'general/general_form.html'
GENERAL_DELETE_TEMPLATE = 'general/general_delete_confirm.html'
HOME_URL = '/'  
LABELS_LIST_URL = reverse_lazy('labels:list')
USERS_LIST_URL = reverse_lazy('users:list')
STATUSES_LIST_URL = reverse_lazy('statuses:list')


class LabelListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'label/label_list.html'


class LabelCreateView(LoginRequiredMixin, CreateView):
    model = Label
    fields = ['name']
    success_url = LABELS_LIST_URL
    template_name = GENERAL_FORM_TEMPLATE


class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    success_url = LABELS_LIST_URL
    template_name = GENERAL_DELETE_TEMPLATE


class StatusListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'status/status_list.html'


class StatusCreateView(LoginRequiredMixin, CreateView):
    model = Status
    fields = ['name']
    success_url = HOME_URL
    template_name = GENERAL_FORM_TEMPLATE


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    fields = ['name']
    success_url = HOME_URL
    template_name = GENERAL_FORM_TEMPLATE


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    success_url = HOME_URL
    template_name = GENERAL_DELETE_TEMPLATE


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('username', 'first_name', 'last_name', 'email')
    template_name = GENERAL_FORM_TEMPLATE
    success_url = USERS_LIST_URL


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    success_url = USERS_LIST_URL
    template_name = GENERAL_DELETE_TEMPLATE

    def test_func(self):
        return self.request.user.is_superuser


class UserCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = get_user_model()
    fields = ('username', 'first_name', 'last_name', 'email', 'password')
    template_name = GENERAL_FORM_TEMPLATE
    success_url = USERS_LIST_URL

    def test_func(self):
        return self.request.user.is_superuser