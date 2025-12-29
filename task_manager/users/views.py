from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import UserForm
from .models import User


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user/list.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Users')
        context['button'] = _('Create user')
        return context


class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'general/general_form.html'
    success_url = reverse_lazy('home')
    success_message = _('User successfully created')

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Create user')
        context['button'] = _('Create')
        return context


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'general/general_form.html'
    success_url = reverse_lazy('home')
    success_message = _('User successfully updated')
    permission_denied_message = _(
        "You don't have permission to edit another user"
    )

    def test_func(self):
        return self.get_object() == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect('home')

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': _('Edit user'),
            'button': _('Update')
        })
        return context


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'general/general_delete_confirm.html'
    success_url = reverse_lazy('home')
    success_message = _('User successfully deleted')
    permission_denied_message = _(
        "You don't have permission to delete another user"
    )
    protected_message = _('Cannot delete user because it is in use')
    protected_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        user = self.request.user    
        return user.is_superuser and obj != user

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect('home')

    def form_valid(self, form):
        try:
            messages.success(self.request, self.success_message)
            return super().form_valid(form)
        except models.ProtectedError:
            messages.error(self.request, self.protected_message)
            return redirect(self.protected_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': _('Delete user'),
            'button': _('Yes, delete')
        })
        return context