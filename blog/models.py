from django.db import models

# Create your models here.

class Blog(models.Model):
    rubric = models.CharField(max_length=255, verbose_name='Рубрика')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    cover_photo = models.ImageField(upload_to='photos/articles/')
    article_head_photo = models.ImageField(upload_to='photos/articles/')
    short = models.TextField(blank=True, verbose_name='Короткое описание')
    text = models.TextField(blank=True, verbose_name='Текст')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'
        ordering = ['time_create', 'title']


