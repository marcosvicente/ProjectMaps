from django.views import generic
from django.views.generic.edit import FormView

from .models import Viagem
from .forms import ViagemForm


class Index(generic.ListView):
    template_name = "index.html"
    model = Viagem


class IndexDetail(generic.DetailView):
    model = Viagem
    template_name = "detail.html"


class Cadastro(FormView):
    form_class = ViagemForm
    template_name = "cadastro.html"

    # Savar dados na tabela Viagem
    def form_valid(request):
        if request.method == 'POST':
            form = ViagemForm(request.POST)
            if form.is_valid():
                novo_viagem = form.save(commit=False)
                novo_viagem.save()
        else:
            form = ViagemForm()
