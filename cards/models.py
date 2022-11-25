from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


# Create your models here.
class Card(models.Model):

    STATUS_CARD = [
        ('INACTIVE', 'card is not active'),
        ('ACTIVE', 'card is active'),
        ('OVERDUE', 'card is overdue')
    ]

    series = models.IntegerField()
    number_regex = RegexValidator(regex=r'^\+?1?\d{16}$', message="Card number must be entered in the format: '9999888877776666'.")
    number = models.CharField(validators=[number_regex], max_length=16, unique=True, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now, verbose_name='created date')
    end_date = models.DateTimeField(default=timezone.now, verbose_name='activity end date',)
    cvv = models.IntegerField()
    balance = models.FloatField(default=0)
    status = models.CharField(max_length=13, choices=STATUS_CARD)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'
