from django.db import models


class Shed(models.Model):
    title = models.CharField('День', max_length=15)
    predmet = models.CharField('Предмет', max_length=25)
    start = models.TimeField('Начало занятия')
    end = models.TimeField('Конец занятия')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
