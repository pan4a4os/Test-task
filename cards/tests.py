from django.test import TestCase
from .models import Card


class MyTest(TestCase):
    fixtures = ["card_data.json"]

    def test_should_create_group(self):
        card = Card.objects.get(pk=43)
        self.assertEqual(card.series, 13)
