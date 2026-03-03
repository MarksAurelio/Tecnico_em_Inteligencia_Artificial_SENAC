from django.shortcuts import render
# função para renderizar o questionário
def abrir_questionario(request):
    return render(request,'questionario/index.html')
