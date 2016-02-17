from django.views import generic

from .models import Viagem


class Index(generic.ListView):
    template_name = "index.html"
    model = Viagem


class IndexDetail(generic.DetailView):
    model = Viagem
    template_name = "detail.html"
