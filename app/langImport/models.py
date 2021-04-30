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
    public = models.BooleanField(default=True)
    # this json_file contains both original text and translated text
    json_file = jsonfield.JSONField()
  
    #displays title and user in the admin section
    def __str__(self):
    	return self.lesson_title + ' | ' + str(self.user_id)
    #returns to lessons page 
    def get_absolute_url(self):
        return reverse('web-lessons')



# English word list
class EnglishWord(models.Model):
    
    word = models.CharField(max_length=20, default = "none")
    definition = models.TextField(max_length=20, default= "none")
    word_class = models.CharField(max_length=20, default = "none")
    pron = models.CharField(max_length=20, default = "none")

    def __str__(self):
        return self.word 
# Russian word list
class RussianWord(models.Model):
    word = models.CharField(max_length=20, default = "none")
    definition = models.TextField(max_length=20, default= "none")
    word_class = models.CharField(max_length=20, default = "none")
    pron = models.CharField(max_length=20, default = "none")

    def __str__(self):
        return self.word 


# French word list
class FrenchWord(models.Model):
    word = models.CharField(max_length=20, default = "none")
    definition = models.TextField(max_length=20, default= "none")
    word_class = models.CharField(max_length=20, default = "none")
    pron = models.CharField(max_length=20, default = "none")

    def __str__(self):
        return self.word


# Spanish word list
class SpanishWord(models.Model):
    word = models.CharField(max_length=20, default = "none")
    definition = models.TextField(max_length=20, default= "none")
    word_class = models.CharField(max_length=20, default = "none")
    pron = models.CharField(max_length=20, default = "none")

    def __str__(self):
        return self.word


# technically these dictionary tables are "above" the word lists in the hierarchy, but they have to be first since
# they need references to the word lists
# English dictionary
class Edictionary(models.Model):
    translation_id = models.AutoField
    word_id = models.ForeignKey(EnglishWord, on_delete=models.CASCADE)
    spa_id = models.ForeignKey(SpanishWord, on_delete=models.CASCADE, related_name="en_lang1")
    ru_id = models.ForeignKey(RussianWord, on_delete=models.CASCADE, related_name="en_lang2")
    fr_id = models.ForeignKey(FrenchWord, on_delete=models.CASCADE, related_name="en_lang3")

    def __str__(self):
        return str(self.word_id)


# Russian dictionary
class Rdictionary(models.Model):
    translation_id = models.AutoField
    word_id = models.ForeignKey(RussianWord, on_delete=models.CASCADE)
    en_id = models.ForeignKey(EnglishWord, on_delete=models.CASCADE, related_name="ru_lang1")
    spa_id = models.ForeignKey(SpanishWord, on_delete=models.CASCADE, related_name="ru_lang2")
    fr_id = models.ForeignKey(FrenchWord, on_delete=models.CASCADE, related_name="ru_lang3")

    def __str__(self):
        return str(self.word_id)


# French dictionary
class Fdictionary(models.Model):
    translation_id = models.AutoField
    word_id = models.ForeignKey(FrenchWord, on_delete=models.CASCADE)
    en_id = models.ForeignKey(EnglishWord, on_delete=models.CASCADE, related_name="fr_lang1")
    spa_id = models.ForeignKey(SpanishWord, on_delete=models.CASCADE, related_name="fr_lang2")
    ru_id = models.ForeignKey(RussianWord, on_delete=models.CASCADE, related_name="fr_lang3")

    def __str__(self):
        return str(self.word_id)


# Spanish dictionary
class Sdictionary(models.Model):
    translation_id = models.AutoField
    word_id = models.ForeignKey(SpanishWord, on_delete=models.CASCADE)
    en_id = models.ForeignKey(EnglishWord, on_delete=models.CASCADE, related_name="spa_lang1")
    ru_id = models.ForeignKey(RussianWord, on_delete=models.CASCADE, related_name="spa_lang2")
    fr_id = models.ForeignKey(FrenchWord, on_delete=models.CASCADE, related_name="spa_lang3")

    def __str__(self):
        return str(self.word_id)


