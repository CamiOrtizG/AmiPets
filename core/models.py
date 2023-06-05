from django.db import models

# Create your models here.

class Region(models.Model):
    nombre_r= models.CharField(max_length=100, verbose_name='Región')

    def __str__(self):
        return self.nombre_r

class Comuna(models.Model):
    nombre_com = models.CharField(max_length=60, verbose_name='Comuna')   
    region = models.ForeignKey(Region, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre_com    
  

class Persona(models.Model):
    rut = models.CharField(max_length = 11, unique=True, verbose_name='Rut')
    dv= models.CharField(max_length=1, verbose_name='digito verificador')
    nombres = models.CharField(max_length = 100, verbose_name='Nombre completo')
    apellidos = models.CharField(max_length=50, verbose_name='Apellidos')
    phone = models.IntegerField( verbose_name="Teléfono")
    mail = models.EmailField(verbose_name="Correo")
    direccion = models.CharField(max_length=70, verbose_name="Dirección")
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)
    

    def __str__(self):
        return self.nombres 


class Sucursal(models.Model):
    nombre_suc = models.CharField(max_length=50, verbose_name='Sucursal')


    def __str__(self):
        return self.nombre_suc
    
class Funcionario(models.Model):
    cargo = models.CharField(max_length=60, verbose_name='Cargo')
    profesion = models.CharField(max_length=60, blank=True, verbose_name= 'Profesion')
    mail_insti= models.EmailField(verbose_name='Correo institucional')
    imagen= models.ImageField(upload_to="funcionarios", null=True, blank=True)
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    sucur= models.ForeignKey(Sucursal, on_delete=models.PROTECT)

    def __str__(self):
        return self.persona.nombres
    
   
opciones_genero =[ 
    [1, "Hembra"],
    [2, "Macho"],
    [3, "Indefinido"]]    

opciones_castracion=[
    [1, "Si"],
    [2, "No"],
    [3, "Por confirmar"]
]
    
class ficha_pet (models.Model):
    nombre_pet = models.CharField(max_length=60, verbose_name='Nombre mascota')
    especie = models.CharField(max_length=10, verbose_name='Especie')
    raza = models.CharField(max_length=20, blank=True, verbose_name='Raza')
    color =models.CharField(max_length=20, verbose_name='Color mascota')
    genero = models.IntegerField(choices=opciones_genero, verbose_name='género')
    edad =models.IntegerField(blank=True, verbose_name='Edad')
    observ= models.TextField(max_length=250, blank=True, verbose_name='Observaciones')
    castrado = models.IntegerField(choices=opciones_castracion, verbose_name='Esterilización')
    imagen= models.ImageField(upload_to="mascotas", null=True)
    contact_emerg = models.CharField(max_length=50, verbose_name='Nombre contacto emergencia')
    num_emerg= models.IntegerField(verbose_name='Número de emergencia')
    dueño= models.ForeignKey(Persona, on_delete=models.PROTECT)

    

    def __str__(self):
        return self.nombre_pet
    
class estado (models.Model):
    descrip_est= models.CharField(max_length=30, verbose_name='Estado reserva')

    def __str__(self):
        return self.descrip_est
    
class reserva (models.Model):
    descrip =models.TextField(max_length=200, verbose_name='Descripción')    
    fecha_ini = models.DateField(verbose_name='Fecha ingreso')
    fecha_term= models.DateField(verbose_name='Fecha salida')
    persona= models.ForeignKey(Persona, on_delete=models.PROTECT)
    estado= models.ForeignKey(estado, on_delete=models.PROTECT)


    def __str__(self):
        return self.persona.nombres
    

class Tarifa(models.Model):
    detalle= models.CharField(max_length=30, verbose_name='Detalle', null=True)    
    valor= models.IntegerField(verbose_name='Valor')

    def __str__(self):
        return self.detalle
    

class estadia (models.Model):
    cant_dias= models.IntegerField(verbose_name='Días de hospedaje')
    descrip_est= models.CharField(max_length=200, verbose_name='Descripción')
    monto_total= models.IntegerField(verbose_name='Monto total')
    fech_pago= models.DateField(verbose_name="fecha pago")
    valor= models.ForeignKey(Tarifa, on_delete=models.PROTECT)
    cliente= models.ForeignKey(reserva, on_delete=models.PROTECT)

    def __str__(self):
        return self.descrip_est

opciones_vacuna=[
    [1,"Si"],
    [2,"No"]
]
class Vacuna(models.Model):
    descrip_vac= models.CharField(max_length=100, verbose_name="Descripción vacunas")
    pendientes= models.IntegerField(choices=opciones_vacuna, verbose_name="Vacunas pendientes")
    mascota= models.ForeignKey(ficha_pet, on_delete=models.PROTECT)


    def __str__(self):
        return self.descrip_vac   


class Hist_pago(models.Model):
    id_estadia= models.IntegerField(verbose_name="id historico pagos estadia")
    fecha_pago= models.DateField(verbose_name="fecha pago")
    monto=models.IntegerField(verbose_name="monto")

class Hist_reserva(models.Model):
    id_hist_est= models.IntegerField(verbose_name="id historico reserva")
    fecha_ini= models.DateField(verbose_name="fecha inicio")
    fecha_term= models.DateField(verbose_name="fecha termino")
    id_cliente= models.IntegerField(verbose_name="id cliente")









