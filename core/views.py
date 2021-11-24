from django.shortcuts import render, redirect
from .forms import contactForm, paceinteForm

# Create your views here.

def base(request):
    return render(request, 'web/base.html')

def index(request):
    return render(request, 'web/index.html')

def passr(request):
    return render(request, 'web/pass.html')

def tomahora(request):
    return render(request, 'web/tomahora.html')

def contact(request): #CONTACTO

    msnform = contactForm()
    data = {'cform' : msnform}
    
    if request.method == 'POST':
        msnform = contactForm(data = request.POST) 
        if msnform.is_valid():
            msnform.save()
        else:
            data["cform"] = msnform;
        
        print("Mensaje enviado Correctamente")
    else:
        print("No se puedo enviar el mensaje, revisa los datos")
        
    return render(request, 'web/contact.html',  data)

def register(request): #REGISTER USER
    paciente = paceinteForm()
    data = {
        'form' : paciente
    }
    paciente = paceinteForm(data=request.POST)
    if request.method == 'POST':
        if paciente.is_valid():
            paciente.save()
            print("te has registrado correctamente")
            return redirect('index')
        else:
            data['form'] = paciente
    else:
        print('error en el formulario')

    return render(request, 'web/register.html', data)
