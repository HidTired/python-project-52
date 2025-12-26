from django.urls import path

from task_manager.views import LabelCreateView, LabelDeleteView, LabelListView

app_name = 'labels'
urlpatterns = [
    path('', LabelListView.as_view(), name='list'),
    path('create/', LabelCreateView.as_view(), name='create'),
    path('<int:pk>/delete/', LabelDeleteView.as_view(), name='delete'),
]
