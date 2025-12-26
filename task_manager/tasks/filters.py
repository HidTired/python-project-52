import django_filters
from django.contrib.auth import get_user_model

from task_manager.labels.models import Label
from task_manager.statuses.models import Status

from .models import Task

User = get_user_model()


class TaskFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all()
    )
    author = django_filters.ModelChoiceFilter(
        queryset=User.objects.all()
    )
    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all()
    )
    labels = django_filters.ModelMultipleChoiceFilter(
        queryset=Label.objects.all()
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'author', 
                 'executor', 'labels']
