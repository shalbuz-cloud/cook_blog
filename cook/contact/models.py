from ckeditor.fields import RichTextField
from django.db import models


class ContactModel(models.Model):
    """Класс модели обратной связи"""
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'


class ContactLink(models.Model):
    """Класс модели контактов"""
    icon = models.FileField(upload_to='icons/')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class About(models.Model):
    """Класс модели страницы о нас"""
    name = models.CharField(max_length=50, default='')
    text = RichTextField()
    short_text = RichTextField()


class ImageAbout(models.Model):
    """Класс модели изображений страницы о нас"""
    image = models.ImageField(upload_to='about/')
    page = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about_images')
    alt = models.CharField(max_length=100)


class Social(models.Model):
    """Класс модели социальных сетей страницы о нас"""
    icon = models.FileField(upload_to='icons/')
    name = models.CharField(max_length=200)
    link = models.URLField()
