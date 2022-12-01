from django.views.generic import CreateView
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.db.models import Q
from django.utils import timezone
from django.urls import reverse_lazy
from .models import Card
from .forms import GenerateCardsForm


def list_of_cards(request):
    cards = Card.objects.order_by('-created_date')
    search_query = request.GET.get('search', '')
    if search_query:
        cards = Card.objects.filter(Q(series__icontains=search_query) |
                                    Q(number__icontains=search_query) |
                                    Q(created_date__icontains=search_query) |
                                    Q(end_date__icontains=search_query) |
                                    Q(status__icontains=search_query))
    DATETIME_FORMAT = 'Y-m-d H:i'
    context = {'cards': cards,
               'search_query': search_query,
               'DATETIME_FORMAT': DATETIME_FORMAT
               }
    return render(request=request, template_name='cards/list_of_cards.html', context=context)


class CardGenerateView(CreateView):
    model = Card
    form_class = GenerateCardsForm
    template_name = 'cards/card_generator.html'
    success_url = reverse_lazy('list')


def profile_card(request, id):
    card = get_object_or_404(Card, id=id)
    DATETIME_FORMAT = 'Y-m-d H:i'
    context = {'card': card,
               'DATETIME_FORMAT': DATETIME_FORMAT
               }
    return render(request=request, template_name='cards/profile_card.html', context=context)


def delete_card(request, id):
    card = Card.objects.get(id=id)
    card.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def change_status_card(request, id):
    card = Card.objects.get(id=id)
    if card.end_date <= timezone.now():
        card.status = "card is overdue"
        card.save()
    elif card.status == 'card is active':
        card.status = 'card is not active'
        card.save()
    else:
        card.status = 'card is active'
        card.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])




