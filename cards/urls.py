from django.urls import path
from . import views
from .views import list_of_cards, CardGenerateView


urlpatterns = [
    path('list/', list_of_cards, name='list'),
    path('generator/', CardGenerateView.as_view(), name='generator'),
    path('profile/<int:id>', views.profile_card, name='profile'),
    path('delete/<int:id>', views.delete_card, name='delete'),
    path('change/<int:id>', views.change_status_card, name='change'),
]
