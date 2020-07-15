from django.shortcuts import render, redirect
from models import Dojo, Ninja

# Create your views here.
def index(request):
    return render(request, 'index.html')

def addDojo(request):
    postName = request.POST['name']
    postCity = request.POST['city']
    postState = request.POST['state']
    newDojo = Dojo.objects.create(name=postName, city=postCity, state=postState)
    return redirect('/')

def addNinja(request):
    postFirstName = request.POST['']