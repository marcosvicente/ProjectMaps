from django.views import generic
from django.views.generic.edit import FormView

from .models import Viagem
from .forms import ViagemForm, OrigemForm, DestinoForm


class Index(generic.ListView):
    template_name = "index.html"
    model = Viagem


class IndexDetail(generic.DetailView):
    model = Viagem
    template_name = "detail.html"


class Cadastro(FormView):
    form_class = ViagemForm
    template_name = "cadastro.html"
    success_url = '/'

    # Savar dados na tabela Viagem
    def form_valid(self, form):
        novo_viagem = form.save(commit=False)
        novo_viagem.save()

        return super(Cadastro, self).form_valid(form)


class CadastroOrigem(FormView):
    form_class = OrigemForm
    template_name = "origem.html"
    success_url = '/cadastro/'

    def form_valid(self, form):
        novo_origem = form.save(commit=False)
        novo_origem.save()
        return super(CadastroOrigem, self).form_valid(form)


class CadastroDestino(FormView):
    form_class = DestinoForm
    template_name = "destino.html"
    success_url = "/cadastro/"

    def form_valid(self, form):
        novo_destino = form.save(commit=False)
        novo_destino.save()
        return super(CadastroDestino, self).form_valid(form)
