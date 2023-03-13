from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField('Название актива', max_length=100)
    task = models.IntegerField('Кол-во')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Актив'
        verbose_name_plural = 'Активы'


