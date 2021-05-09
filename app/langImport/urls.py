from django.contrib import admin
from django.urls import path
from . import views
from .views import LessonView, ReadView, HomeView, EditLessonView, DeleteLessonView

urlpatterns = [
    path('', HomeView.as_view(), name='web-home'),
    path('import/', views.import_page, name='web-import'),
    path('about/', views.about_page, name='web-about'),
    path('help/', views.help_page, name='web-help'),
    path('lessons/', LessonView.as_view(), name= 'web-lessons'),
    path('read/<int:pk>', ReadView.as_view(), name='web-read'),
    path('settings/', views.settings, name= 'web-settings'),
    path('lessons/edit/<int:pk>', EditLessonView.as_view(), name='edit-lesson' ),
    path('lessons/<int:pk>/delete', DeleteLessonView.as_view(), name='delete-lesson' )
]
