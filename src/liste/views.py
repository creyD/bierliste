from django.shortcuts import render

# Create your views here.


def startbildschirm(request):
    return render(request, 'liste/home.html')
