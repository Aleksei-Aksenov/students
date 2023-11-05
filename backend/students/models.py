from django.db import models


class Student(models.Model):
    name = models.CharField(
        max_length=140,
        verbose_name='ФИО',
    )
    group = models.CharField(
        max_length=140,
        verbose_name='Группа',
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return self.name
