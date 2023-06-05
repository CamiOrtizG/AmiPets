from django.shortcuts import render, redirect, get_object_or_404
from requests import request
from .forms import PersonaForm, FichapetForm, FuncionarioForm, ReservaForm, EstadiaForm, VacunaForm
from .models import Persona, ficha_pet, Funcionario, Tarifa, reserva, estado, Vacuna
from django.contrib import messages
from datetime import date
import json
# Create your views here.


def home(request):
    return render(request, 'core/home.html')

def acceso(request):
    return render(request, 'core/acceso.html')

def Reserva(request):
    data = {
        'form': ReservaForm()
    }
    if request.method == 'POST':
        formulario = ReservaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado con éxito")
        else:
            data['form'] = formulario
            

    return render(request, 'core/reserva.html', data)

def listaReserva(request):
    reservas = reserva.objects.all()

    data = {
        'reservas' : reservas
    }
    return render (request,'core/listar/lista_reserva.html', data)

def modificarReservas(request, id):
    
    reservas = get_object_or_404(reserva, id=id)

    data = {
        'form': ReservaForm(instance=reservas)
        }
    if request.method == 'POST':
        formulario = ReservaForm(data=request.POST, instance=reservas)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect (to="lista_reserva")
        data["form"] = formulario
    
    return render (request, 'core/listar/modificarReserva.html', data)

# agregar huesped
def huesped(request):
    data = {
        'form': FichapetForm()
    }
    if request.method == 'POST':
        formulario = FichapetForm(data=request.POST, files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Huesped ingresado correctamente")
            return redirect (to="listarHuesped")
            
        else:
            data["form"] = formulario

    return render(request, 'core/huesped.html', data)


def cliente(request):
    data = {
        'form': PersonaForm
    }
    if request.method == 'POST':
        formulario = PersonaForm(data= request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Cliente ingresado correctamente")
            return redirect (to="huesped")

        else:
            data["form"] = formulario

    return render(request, 'core/cliente.html', data)

def base(request):
    return render(request, 'core/base.html')


def index(request):
    return render(request, 'core/index.html')

def listarCliente(request):
    clientes = Persona.objects.all()

    data = {
        'clientes' : clientes
    }
    return render (request,'core/listar/listar.html', data)


def listarHuesped(request):
    huespedes = ficha_pet.objects.all()

    data = {
        'huespedes' : huespedes
    }
    return render (request,'core/listar/listarHuesped.html', data)


def funcionario(request):

        data = {
        'form1': FuncionarioForm()
        }

        if request.method == 'POST':
            formulario = FuncionarioForm(data=request.POST, files= request.FILES)
            if formulario.is_valid():
                formulario.save()
                data["mensaje1"] = "guardado"
            else:
                data['form1'] = formulario


        return render(request, 'core/funcionario.html', data)

def listarFuncionarios(request):
    funcionarios = Funcionario.objects.all()

    data = {
        'funcionarios' : funcionarios 
    }
    return render (request,'core/listar/listarFuncionarios.html', data)

def modificarCliente(request, id):
    
    persona = get_object_or_404(Persona, id=id)

    data = {
        'form': PersonaForm(instance=persona)
        }
    if request.method == 'POST':
        formulario = PersonaForm(data=request.POST, instance=persona, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect (to="listar")
        data["form"] = formulario
    
    return render (request, 'core/listar/modificarCliente.html', data)


def modificarHuesped(request, id):

    huesped = get_object_or_404(ficha_pet, id=id)

    data = {
        'form' : FichapetForm(instance=huesped)
        }
    if request.method == 'POST':
        formulario = FichapetForm(data=request.POST, instance=huesped, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect (to="listarHuesped")
        data['form'] = formulario

    return render (request, 'core/listar/modificarHuesped.html', data )

  
def calcularTarifa(request):
    
    if request.method == 'POST':
        try:
            numero = int(request.POST.get('numero'))
            tarifa_id = int(request.POST.get('tarifa'))
            tarifa = Tarifa.objects.get(pk=tarifa_id)
            resultado = tarifa.valor * numero
            
            data = {
                'tarifa': tarifa,
                'numero': numero,
                'resultado': resultado,
            }
        except Exception as e:
            print(e)
            data = {
                'tarifas':Tarifa.objects.all(),                
                'warning': messages.warning (request,'Por favor ingresa un valor'),
            }
            return render(request, 'core/tarifa/calcular_tarifa.html', data)
        return render(request, 'core/tarifa/resultado.html', data)

    tarifas = Tarifa.objects.all()
    data = {'tarifas': tarifas}
    return render(request, 'core/tarifa/calcular_tarifa.html', data)

def base2(request):
    return render(request, 'core/base2.html')

def nosotros(request):
    tarifas = Tarifa.objects.all()

    context = {
        'tarifas': tarifas
        }
    return render(request, 'core/nosotros.html', context)

def agendar (request):
    today = date.today()
    fecha_ini = reserva.objects.all()
    resultado_reservas = list(fecha_ini.values())
    print('resultado_reservas:', resultado_reservas)
    reservas = []
    for item in resultado_reservas:
        persona = Persona.objects.get(pk=item['persona_id'])
        estados = estado.objects.get(pk=item ['estado_id'])
        res = {
            'estado': estados.descrip_est,
            'nombre_persona': persona.nombres,
            'fecha_ini': item['fecha_ini'].strftime('%Y-%m-%d'),
            'fecha_term': item['fecha_term'].strftime('%Y-%m-%d')
        }
        reservas.append(res)
    print('reservas:', reservas)
    return render(request, 'core/agenda.html', {'reserva_hoy': reservas})
   
def estadia(request):
    data = {
    'form': EstadiaForm()
    }

    if request.method == 'POST':
        formulario = EstadiaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje1"] = "guardado"
        else:
            data['form'] = formulario


    return render(request, 'core/estadia.html', data)

def vacunas(request):
    data = {
        'form': VacunaForm()
    }
    if request.method == 'POST':
        formulario = VacunaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado con éxito")
        else:
            data['form'] = formulario
    return render(request, 'core/vacuna.html', data)

def listar_vacunas (request):
    Vacunas = Vacuna.objects.all()

    data = {
        'Vacunas' : Vacunas 
    }
    return render(request, 'core/listar/listar_vacuna.html', data)


def modificarVacuna(request, id):
    vacunas = get_object_or_404(Vacuna, id=id)
    data = {
        'form': VacunaForm(instance=vacunas)
        }
    if request.method == 'POST':
        formulario = VacunaForm(data=request.POST, instance=vacunas)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "prueba")
            return redirect(to="listar_vacuna")
        data["form"] = formulario   
    return render (request, 'core/listar/modificarVacuna.html', data)




   




    