from django.http import HttpResponse

def home(request):
    """Главная страница с приветствием"""
    return HttpResponse("Приветствие от hexlet-code! Готово к разработке task_manager.")