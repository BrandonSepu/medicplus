from django.shortcuts import render
from .forms import contactForm

# Create your views here.

def base(request):
    return render(request, 'web/base.html')

def index(request):
    return render(request, 'web/index.html')

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

