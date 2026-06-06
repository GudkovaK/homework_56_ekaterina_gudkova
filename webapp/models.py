from django.db import models

# Create your models here.
STATUS_CHOICES = [
    ('active', 'Активно'),
    ('blocked', 'Заблокировано'),
]

class GuestEntry(models.Model):
    name = models.CharField(max_length=100, verbose_name = 'Имя')
    email = models.EmailField(verbose_name = 'почта')
    text = models.TextField(verbose_name='текст')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active',
        verbose_name='Статус'
    )

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return self.name