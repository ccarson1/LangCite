from django.contrib import admin
from .models import Lesson
from .models import Language
from .models import Genre
from .models import EnglishWord
from .models import RussianWord
from .models import SpanishWord
from .models import FrenchWord
from .models import Edictionary
from .models import Rdictionary
from .models import Fdictionary
from .models import Sdictionary


admin.site.register(Lesson)
admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(EnglishWord)
admin.site.register(RussianWord)
admin.site.register(SpanishWord)
admin.site.register(FrenchWord)
admin.site.register(Edictionary)
admin.site.register(Rdictionary)
admin.site.register(Fdictionary)
admin.site.register(Sdictionary)
