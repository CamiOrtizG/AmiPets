from django.urls import path, include
from .views import home,base,acceso, Reserva,huesped,cliente, agendar, index, listarCliente, listarHuesped, funcionario, listarFuncionarios, modificarCliente, modificarHuesped,calcularTarifa, base2, nosotros, estadia, listaReserva, modificarReservas, vacunas, listar_vacunas, modificarVacuna
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', index, name="index"),
    path('acceso/', login_required (acceso), name="acceso"),    
    path('reserva/', login_required (Reserva), name="reserva"),
    path('huesped/', login_required(huesped), name="huesped"),
    path('cliente/', login_required(cliente), name="cliente"),
    path('base/', login_required(base), name='base'),
    path('agenda/', login_required (agendar), name='agenda'),
    path('home/', login_required(home), name='home'),
    path('listar/', login_required(listarCliente), name='listar'),
    path('listarHuesped/', login_required(listarHuesped), name='listarHuesped'),
    path('funcionario/', login_required(funcionario), name='funcionario'),
    path('listarFuncionarios/', login_required(listarFuncionarios), name='listarFuncionarios'),
    path('modificarCliente/<id>/', login_required(modificarCliente), name='modificarCliente'),
    path('modificarHuesped/<id>/', login_required(modificarHuesped), name='modificarHuesped'),
    path('calcular_tarifa/', login_required(calcularTarifa), name='calcular_tarifa'),
    path('resultado/', login_required(calcularTarifa), name='resultado'),
    path('nosotros/', nosotros, name='nosotros'),
    path('base2/',base2, name='base2'),
    path('estadia/', login_required(estadia), name='estadia'),
    path('lista_reserva/', login_required(listaReserva), name='lista_reserva'),
    path('modificarReserva/<id>/', login_required(modificarReservas), name='modificarReserva'),
    path('vacuna/', login_required(vacunas), name='vacuna'),
    path('listar_vacuna/', login_required(listar_vacunas), name='listar_vacuna'),
    path('modificarVacuna/<id>/', login_required(modificarVacuna), name='modificarVacuna'),
    
    ]