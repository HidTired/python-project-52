from pathlib import Path
from task_manager.settings import *

SECRET_KEY = 's7#-677h7o46avn74op0@r_d&fwz)ys%0jx%6(mcw29$$3b(wy'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

ROOT_URLCONF = 'task_manager.urls'
