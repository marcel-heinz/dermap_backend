from django.shortcuts import render


# Create your views here.

def index(request):
    title = 'Home'
    return render(request, 'pages/index.html', {'title': title})


def imprint(request):
    title = 'Imprint'
    return render(request, 'pages/imprint.html', {'title': title})


def tac(request):
    # Terms and Conditions
    # TODO Test
    title = 'Terms and Conditions'

    return render(request, 'pages/tac.html', {'title': title})
