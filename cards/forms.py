import random
from django import forms
from .models import Card
from django.utils import timezone
from django.forms import NumberInput


class GenerateCardsForm(forms.ModelForm):
    series = forms.IntegerField()
    count = forms.IntegerField()


    class Meta:
        model = Card
        fields = ['series', 'count']

        widgets = {
            'series': NumberInput(attrs={'class': 'form_control'}),
            'count': NumberInput(attrs={'class': 'form_control'})
        }

    def save(self, commit=True):
        cleaned_series = self.cleaned_data.pop('series')
        cleaned_count = self.cleaned_data.pop('count')

        objects_to_create = [
            Card(series=cleaned_series,
                 number=random.randint(1000000000000000, 9999999999999999),
                 created_date=timezone.now(),
                 end_date=timezone.now() + timezone.timedelta(days=365),
                 cvv=random.randint(1, 999),
                 balance=0.0,
                 status='card is inactive')
            for i in range(0, cleaned_count)
        ]

        Card.objects.bulk_create(objects_to_create)

        return Card.objects.last()
