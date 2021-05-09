# Generated by Django 3.1.4 on 2021-05-09 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('langImport', '0022_tdictionary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tdictionary',
            name='en_id',
        ),
        migrations.RemoveField(
            model_name='tdictionary',
            name='fr_id',
        ),
        migrations.RemoveField(
            model_name='tdictionary',
            name='ru_id',
        ),
        migrations.RemoveField(
            model_name='tdictionary',
            name='spa_id',
        ),
        migrations.DeleteModel(
            name='EnglishWord',
        ),
        migrations.DeleteModel(
            name='FrenchWord',
        ),
        migrations.DeleteModel(
            name='RussianWord',
        ),
        migrations.DeleteModel(
            name='SpanishWord',
        ),
        migrations.DeleteModel(
            name='Tdictionary',
        ),
    ]