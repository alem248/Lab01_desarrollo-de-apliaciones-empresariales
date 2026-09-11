from django.shortcuts import render


def sumar(request, a, b):
    contexto = {
        'operacion': 'suma',
        'signo': '+',
        'a': a,
        'b': b,
        'resultado': a + b,
    }
    return render(request, 'calculadora/resultado.html', contexto)


def restar(request, a, b):
    contexto = {
        'operacion': 'resta',
        'signo': '-',
        'a': a,
        'b': b,
        'resultado': a - b,
    }
    return render(request, 'calculadora/resultado.html', contexto)


def multiplicar(request, a, b):
    contexto = {
        'operacion': 'multiplicación',
        'signo': '*',
        'a': a,
        'b': b,
        'resultado': a * b,
    }
    return render(request, 'calculadora/resultado.html', contexto)
