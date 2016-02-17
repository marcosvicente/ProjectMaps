from django.views import generic

from .models import Viagem


class Index(generic.ListView):
    template_name = "index.html"
    model = Viagem
