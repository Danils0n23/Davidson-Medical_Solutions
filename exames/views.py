from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import TiposExames


@login_required
def solicitar_exames(request):
    tipos_exames = TiposExames.objects.all()
    if request.method == "GET":
        return render(request, 'solicitar_exames.html', {'tipos_exames': tipos_exames})
    elif request.method == "POST":
        exames_id = request.POST.getlist('exames')
        solicitacao_exames = TiposExames.objects.filter(id__in=exames_id)

        #TODO: Calcular preco dos dados disponíveis

        preco_total = 0
        for i in solicitacao_exames:
            if i.disponivel:
             preco_total += i.preco

            print(preco_total)

        return render(request, 'solicitar_exames.html', {'tipos_exames':tipos_exames,'solicitacao_exames': solicitacao_exames, 'preco_total':preco_total}) 