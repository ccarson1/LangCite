# Generated by Django 3.1.4 on 2021-04-01 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('langImport', '0005_lesson_public'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='genre_id',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='language_id',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.DeleteModel(
            name='Lesson',
        ),
    ]
