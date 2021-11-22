from django.db import models
from django.utils import timezone

#TABLAS DE DIRECCION - PAIS/REGION/COMUNA/ADRESS
#PAIS
class pais(models.Model):
    
    nomPais = models.CharField(max_length=50)

    def __str__(self):
        return self.nomPais

#REGION  
class region(models.Model):

    fkPais = models.ForeignKey(pais, on_delete=models.CASCADE)
    nomRegion = models.CharField(max_length=50)

    def __str__(self):
        return self.nomRegion

#COMUNA
class comuna(models.Model):

    fkRegion = models.ForeignKey(region, on_delete=models.CASCADE)
    nomComuna = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nomComuna

# TABLA GENERO
class gender(models.Model):
    nomGender = models.CharField( max_length = 10)

    def __str__(self):
        return self.nomGender

# TABLA PACIENTE
class paciente(models.Model):
    
    nomPac = models.CharField( max_length=50)
    aPatPac = models.CharField( max_length=50)
    rutPac = models.CharField( max_length=50)
    emailPac = models.CharField( max_length=50)
    bornDatePAc = models.DateTimeField(auto_now_add=False,auto_now=False,null=True,blank=True);
    fkGender = models.ForeignKey(gender, on_delete=models.CASCADE, blank=True)
    fkComuna = models.ForeignKey(comuna, on_delete=models.CASCADE)
    adressPac = models.CharField(max_length=70)


    def __str__(self):
        return self.nameContact

# TABLA CONTACTO
class usercontact(models.Model):
    
    nameContact = models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    msn = models.TextField( max_length=400)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nameContact

# TABLA AREA MEDICA
class areaMedica(models.Model):

    nomAMedica = models.CharField( max_length=50)

    def __str__(self):
        return self.nomAMedica

# TABLA DOCTOR
class doctor(models.Model):

    nomDoc = models.CharField( max_length=50)
    aPatDoc = models.CharField( max_length=50)
    rutDoc = models.CharField( max_length=50)
    emailDoc = models.CharField( max_length=50)
    bornDateDoc = models.DateTimeField(auto_now_add=False,auto_now=False,null=True,blank=True);
    fkGender = models.ForeignKey(gender, on_delete=models.CASCADE, blank=True)
    fkComuna = models.ForeignKey(comuna, on_delete=models.CASCADE)
    fkAMedica = models.ForeignKey(areaMedica, on_delete=models.CASCADE)
    adressDoc = models.CharField(max_length=70)

    def __str__(self):
        return self.nomDoc

# TABLA SECRETARIA
class secretaria(models.Model):
    
    nomSec = models.CharField( max_length=50)
    aPatSec = models.CharField( max_length=50)
    rutSec = models.CharField( max_length=50)
    emailSec = models.CharField( max_length=50)
    bornDateSec = models.DateTimeField(auto_now_add=False,auto_now=False,null=True,blank=True);
    fkGender = models.ForeignKey(gender, on_delete=models.CASCADE, blank=True)
    fkComuna = models.ForeignKey(comuna, on_delete=models.CASCADE)
    adressSec = models.CharField(max_length=70)

    def __str__(self):
        return self.nomSec

# TABLA TIPO PAGO      
class tipoPago(models.Model):

    tipoPag = models.CharField( max_length=50)

    def __str__(self):
        return self.tipoPag

# TABLA PAGO
class pago(models.Model):

    fkAreaMedica = models.ForeignKey(areaMedica, on_delete=models.CASCADE)
    valorPAg =  models.IntegerField()

    def __str__(self):
        return self.valorPAg

# TABLA HORA MDEICA
class horaMedica(models.Model):

    consulta = models.CharField( max_length=100)
    hora = models.CharField( max_length=5)
    fecha = models.DateTimeField(auto_now_add=False,auto_now=False,null=False,blank=True);
    fkPaciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    fkTipoPago = models.ForeignKey(tipoPago, on_delete=models.CASCADE)
    fkPago = models.ForeignKey(pago, on_delete=models.CASCADE)
    fkMedico = models.ForeignKey(doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.consulta

# TABLA INFORME
class informe(models.Model):

    fechaIfo = models.DateTimeField(default=timezone.now)
    fkSecretaria = models.ForeignKey(secretaria, on_delete=models.CASCADE)
    fkHoraMedica = models.ForeignKey(horaMedica, on_delete=models.CASCADE)
    comision = models.IntegerField();

    def __str__(self):
        return self.fechaIfo

class comprobante(models.Model):

    fechaComPago = models.DateTimeField(default=timezone.now)
    fkHoraMedica = models.ForeignKey(horaMedica, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.fechaComPago

    