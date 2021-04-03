from django.contrib import admin
from .models import Lesson
from .models import Language
from .models import Genre


admin.site.register(Lesson)
admin.site.register(Language)
admin.site.register(Genre)
