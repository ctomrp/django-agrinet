from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import formulario


# Create your views here.
def mostrar_formulario(request):
    return render(request, 'form.html')


def productor(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        rut = request.POST['rut']
        dv_rut = request.POST['dv']
        nombre = request.POST['primer-nombre']
        apellido = request.POST['apellido-paterno']
        edad = request.POST['edad']
        correo = request.POST['correo']
        telefono = request.POST['telefono']
        razon_social = request.POST['razon-social']
        tipo_productor = request.POST['tipo-productor']

        # Crear instancia del modelo y guardar en la base de datos
        formulario = formulario(
            rut=rut,
            dv_rut=dv_rut,
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            correo=correo,
            telefono=telefono,
            razon_social=razon_social,
            tipo_productor=tipo_productor
        )
        formulario.save()

        return redirect('formulario')  # Puedes redirigir a donde desees después de guardar

    return render(request, 'producer_application/form.html')