from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Create your views here.
def index(request):
    context = {
        'dojos': Dojo.objects.all(),
    }
    return render(request, 'index.html', context)

def addDojo(request):
    postName = request.POST['name']
    postCity = request.POST['city']
    postState = request.POST['state']
    newDojo = Dojo.objects.create(name=postName, city=postCity, state=postState)
    return redirect('/')

def addNinja(request):
    postFirstName = request.POST['first_name']
    postLastName = request.POST['last_name']
    postDojo = Dojo.objects.get(name=request.POST['dojo'])
    newNinja = Ninja.objects.create(first_name=postFirstName, last_name=postLastName, dojo=postDojo)
    return redirect('/')

def delete(request):
    dojoId = int(request.POST['dojo_id'])
    postDojo = Dojo.objects.get(id=dojoId)
    postDojo.delete()
    return redirect('/')