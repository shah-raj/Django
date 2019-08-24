from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Credential,Feedback

def main(request):
    template = loader.get_template('games/main.html')
    return HttpResponse(template.render({}, request))

def contact(request):


    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        feedback = request.POST['feedback']

        raj = Feedback(username=username,email=email,feedback=feedback)
        raj.save()
        return render(request, 'games/confirm.html')
    else:
        return render(request, 'games/contact.html')


def about(request):
    template = loader.get_template('games/about.html')
    return HttpResponse(template.render({}, request))


def index(request):

    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        raj = Credential(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
        raj.save()
        return render(request, 'games/index.html')
    else:
        return render(request, 'games/index.html')
