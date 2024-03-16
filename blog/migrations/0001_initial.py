# Generated by Django 5.0.3 on 2024-03-16 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rubric', models.CharField(max_length=255, verbose_name='Рубрика')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='slug')),
                ('cover_photo', models.ImageField(upload_to='photos/articles/')),
                ('article_head_photo', models.ImageField(upload_to='photos/articles/')),
                ('short', models.TextField(blank=True, verbose_name='Короткое описание')),
                ('text', models.TextField(blank=True, verbose_name='Текст')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Создание')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликован')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи Блога',
                'ordering': ['time_create', 'title'],
            },
        ),
    ]
