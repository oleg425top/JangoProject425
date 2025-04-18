from django.db import models
from django.conf import settings

from users.models import NULLABLE


class Breed(models.Model):
    name = models.CharField(max_length=100, verbose_name='breed')
    description = models.CharField(max_length=1000, verbose_name='description')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'bread'
        verbose_name_plural = 'breeds'


class Dog(models.Model):
    name = models.CharField(max_length=250, verbose_name='dog name')
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, verbose_name='breed')
    photo = models.ImageField(upload_to='dogs/', **NULLABLE, verbose_name='image')
    birth_date = models.DateTimeField(**NULLABLE, verbose_name='birth date')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='хозяин')

    def __str__(self):
        return f'{self.name} ({self.breed})'

    class Meta:
        verbose_name = 'собака'
        verbose_name_plural = 'собаки'


        # abstract = True
        # app_label = 'dogs'
        # ordering = [-1]
        # proxy = True
        # permissions = []
        # db_table = 'doggies'
        # get_latest_by = 'birth_date'
