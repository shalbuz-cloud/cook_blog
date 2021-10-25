from django.db import models


class Photo(models.Model):
    """Класс модели галереи"""
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='gallery/')
    caption = models.TextField(max_length=250, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Gallery(models.Model):
    """Модель галереи"""
    name = models.CharField(max_length=250)
    image = models.ManyToManyField(Photo)
    caption = models.TextField(max_length=250, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'
