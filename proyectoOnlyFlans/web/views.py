from django.shortcuts import render, HttpResponseRedirect
from .models import Flan, ContactForm
from .forms import ContactFormModelForm

# Create your views here.
def indice(request):
    public_flans = Flan.objects.filter(is_private=False)
    context = {
        'public_flans':public_flans
    }
    return render(request, 'index.html', context)

def acerca(request):
    return render(request, 'about.html', {})

def bienvenido(request):
    private_flans = Flan.objects.filter(is_private=True)
    context = {
        'private_flans':private_flans
    }
    return render(request, 'welcome.html', context)

def contacto(request):
    
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        #chequear que los datos son validos
        if form.is_valid():
            #Creamos los datos del formulario
            contact_form = ContactForm.objects.create(**form.cleaned_data) 
            return HttpResponseRedirect('/exito/')
    else:
        form = ContactFormModelForm()
    #el contexto, es el diccionario donde se envian los datos
    context = {'form':form}
    return render(request, 'contacto.html', context)

    
def exito(request):
    return render(request, 'exito.html')