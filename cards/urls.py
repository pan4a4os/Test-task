from django.urls import path
from .views import list_of_cards, CardGenerateView, profile_card, delete_card, change_status_card


urlpatterns = [
    path('list/', list_of_cards, name='list'),
    path('generator/', CardGenerateView.as_view(), name='generator'),
    path('profile/<int:id>', profile_card, name='profile'),
    path('delete/<int:id>', delete_card, name='delete'),
    path('change/<int:id>', change_status_card, name='change'),
]
