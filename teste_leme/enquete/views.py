from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Pergunta,opcoes,Titulo
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum, Max


@csrf_exempt
def IndexView(request):
    titulo = Titulo.objects.all()
    titulo = titulo[0]
    pergunta = Pergunta.objects.all()
    elementos = request.POST

    # pega o ID's das alternativas caso formulário esteja incompleto
    incompleto = []
    for item in elementos.values():
        incompleto.append(int(item))

    elementos = list({int(value) for key, value in elementos.items()})

    # caso o usuário não responda todas as perguntas:
    if len(elementos) != Pergunta.objects.count():
        contexto1 = {'pergunta':pergunta,'incompleto':incompleto,'titulo':titulo}

        #Alerta de mensagem de erro:
        if len(elementos) != 0:
            contexto1['alerta'] = 'Complete o Formulário!'
        return render(request,'enquete/index.html',contexto1)

    # se tudo ok soma os votos de determinada alternativa:
    else:
        obj = opcoes.objects.values_list('id')
        obj = [x[0] for x in obj]
        for i in elementos:
                if i in obj:
                    x = opcoes.objects.get(pk=i)
                    x.votes += 1
                    x.save() 
        y = Titulo.objects.get(titulo=Titulo.objects.all()[0])
        y.total += 1
        y.save() 
        return render(request,'enquete/decisao.html')

def retornar(request):
    return HttpResponseRedirect(request.META["HTTP_REFERER"])

def resultado(request):
    pergunta2 = Pergunta.objects.all()
    total = opcoes.objects.aggregate(Sum('votes'))
    iteration = list(range(1,len(pergunta2)+1))
    total = Titulo.objects.values('total')[0]
    total = total['total']
    top_opt= []
    top_vote = []
    pergs = []

    for opt in pergunta2:
        pergs.append(str(opt))
        max1 = str(opt.opcoes_set.all().order_by('votes').last())
        max2 = opt.opcoes_set.all().aggregate(Max('votes'))
        top_vote.append(max2['votes__max'])
        top_opt.append(max1)

    return render(request,'enquete/resultado.html',{'total':total,
    'top_opt':top_opt,
    'top_vote':top_vote,
    'iteration':zip(iteration,pergs,top_vote,top_opt),
    'pergunta2':pergunta2,
    })




