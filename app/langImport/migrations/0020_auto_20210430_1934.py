# Generated by Django 3.1.4 on 2021-04-30 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('langImport', '0019_auto_20210424_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tdictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lang1', to='langImport.englishword')),
                ('fr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lang4', to='langImport.frenchword')),
                ('ru_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lang3', to='langImport.russianword')),
                ('spa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lang2', to='langImport.spanishword')),
            ],
        ),
        migrations.RemoveField(
            model_name='fdictionary',
            name='en_id',
        ),
        migrations.RemoveField(
            model_name='fdictionary',
            name='ru_id',
        ),
        migrations.RemoveField(
            model_name='fdictionary',
            name='spa_id',
        ),
        migrations.RemoveField(
            model_name='fdictionary',
            name='word_id',
        ),
        migrations.RemoveField(
            model_name='rdictionary',
            name='en_id',
        ),
        migrations.RemoveField(
            model_name='rdictionary',
            name='fr_id',
        ),
        migrations.RemoveField(
            model_name='rdictionary',
            name='spa_id',
        ),
        migrations.RemoveField(
            model_name='rdictionary',
            name='word_id',
        ),
        migrations.RemoveField(
            model_name='sdictionary',
            name='en_id',
        ),
        migrations.RemoveField(
            model_name='sdictionary',
            name='fr_id',
        ),
        migrations.RemoveField(
            model_name='sdictionary',
            name='ru_id',
        ),
        migrations.RemoveField(
            model_name='sdictionary',
            name='word_id',
        ),
        migrations.DeleteModel(
            name='Edictionary',
        ),
        migrations.DeleteModel(
            name='Fdictionary',
        ),
        migrations.DeleteModel(
            name='Rdictionary',
        ),
        migrations.DeleteModel(
            name='Sdictionary',
        ),
    ]
