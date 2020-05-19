from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Category model for posts"""
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, verbose_name='Урл', unique=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tag(models.Model):
    """Tag model for posts"""
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.SlugField(max_length=150, verbose_name='Урл', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']


class Post(models.Model):
    """Post model with 2 different relations (Category and Tag)"""
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, verbose_name='Урл', unique=True)
    author = models.CharField(max_length=100, verbose_name='Автор')
    content = models.TextField(blank=True, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото')
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')

    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(to=Tag, blank=True, related_name='posts')

    def get_absolute_url(self, slug):
        return reverse('post', kwargs={'slug': slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']
