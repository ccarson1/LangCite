from django.db import models
from django.contrib.auth.models import User
import jsonfield 
from django.urls import reverse

# Languages table
class Language(models.Model):
    language_name = models.CharField(max_length=20)

    def __str__(self):
    	return self.language_name

# Genres table
class Genre(models.Model):
    genre_name = models.CharField(max_length=10)
    
    def __str__(self):
    	return self.genre_name

# Lessons table
class Lesson(models.Model):
    
    lesson_title = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)
    # this json_file contains both original text and translated text
    json_file = jsonfield.JSONField()
  
    #displays title and user in the admin section
    def __str__(self):
    	return self.lesson_title + ' | ' + str(self.user_id)
    #returns to lessons page 
    def get_absolute_url(self):
        return reverse('web-lessons')


