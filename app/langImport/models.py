from django.contrib.auth.models import User
from django.db import models


# Languages table
class Languages(models.Model):
    language_id = models.AutoField
    language_name = models.CharField(max_length=20)


# Genres table
class Genres(models.Model):
    genre_id = models.AutoField
    genre_name = models.CharField(max_length=10)


# steps to import lessons stuff
# ---the user imports the file
# (this part I'm a bit iffy on, will clarify later)
# --check if words are in database
#    - if so, then easy translate them
#    - if not, after easy translation, grab from google translate api, add to database and to json
# ---save the json file to imports
# ---create new lesson entry in the db using the json, and the user provided info

# Lessons table
class Lessons(models.Model):
    lesson_id = models.AutoField
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    language_id = models.ForeignKey(Languages, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genres, on_delete=models.CASCADE)
    public = models.BooleanField
    # this json_file contains both original text and translated text
    json_file = models.FileField


# English word list
class EnglishWords(models.Model):
    word_id = models.AutoField
    word = models.CharField
    definition = models.TextField
    word_class = models.CharField
    pron = models.CharField


# Russian word list
class RussianWords(models.Model):
    word_id = models.AutoField
    word = models.CharField
    definition = models.TextField
    word_class = models.CharField
    pron = models.CharField


# French word list
class FrenchWords(models.Model):
    word_id = models.AutoField
    word = models.CharField
    definition = models.TextField
    word_class = models.CharField
    pron = models.CharField


# Spanish word list
class SpanishWords(models.Model):
    word_id = models.AutoField
    word = models.CharField
    definition = models.TextField
    word_class = models.CharField
    pron = models.CharField


# technically these dictionary tables are "above" the word lists in the hierarchy, but they have to be first since
# they need references to the word lists
# English dictionary
class ENDictionary(models.Model):
    translation_id = models.AutoField
    word_id = models.ForeignKey(EnglishWords, on_delete=models.CASCADE)
    lang_1 = models.ForeignKey(Languages, on_delete=models.CASCADE, related_name="en_lang1")
    lang_2 = models.ForeignKey(Languages, on_delete=models.CASCADE, related_name="en_lang2")
    lang_3 = models.ForeignKey(Languages, on_delete=models.CASCADE, related_name="en_lang3")


# Russian dictionary
class RUDictionary(models.Model):
    translation_id = models.AutoField
    word_id = models.ForeignKey(RussianWords, on_delete=models.CASCADE)
    lang_1 = models.ForeignKey(Languages, on_delete=models.CASCADE, related_name="ru_lang1")
    lang_2 = models.ForeignKey(Languages, on_delete=models.CASCADE, related_name="ru_lang2")
    lang_3 = models.ForeignKey(Languages, on_delete=models.CASCADE, related_name="ru_lang3")


# French dictionary
class FRDictionary(models.Model):
    translation_id = models.AutoField
    word_id = models.ForeignKey(FrenchWords, on_delete=models.CASCADE)
    lang_1 = models.ForeignKey(Languages, on_delete=models.CASCADE, related_name="fr_lang1")
    lang_2 = models.ForeignKey(Languages, on_delete=models.CASCADE, related_name="fr_lang2")
    lang_3 = models.ForeignKey(Languages, on_delete=models.CASCADE, related_name="fr_lang3")


# Spanish dictionary
class SPADictionary(models.Model):
    translation_id = models.AutoField
    word_id = models.ForeignKey(SpanishWords, on_delete=models.CASCADE)
    lang_1 = models.ForeignKey(Languages, on_delete=models.CASCADE, related_name="spa_lang1")
    lang_2 = models.ForeignKey(Languages, on_delete=models.CASCADE, related_name="spa_lang2")
    lang_3 = models.ForeignKey(Languages, on_delete=models.CASCADE, related_name="spa_lang3")
