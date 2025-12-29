from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('task_manager.users.urls')),
    path('statuses/', include('task_manager.statuses.urls')),
    path('tasks/', include('task_manager.tasks.urls')),
    path('labels/', include('task_manager.labels.urls')),
]

urlpatterns += i18n_patterns(
    path('', TemplateView.as_view(template_name='index.html'),
        name='home'),
    path('set_language/', include('django.conf.urls.i18n')), 
)

if settings.DEBUG:
    urlpatterns += static(
    settings.STATIC_URL, 
    document_root=settings.STATIC_ROOT
)