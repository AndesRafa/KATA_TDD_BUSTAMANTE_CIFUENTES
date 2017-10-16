from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import TiposDeServicio, Trabajador, TrabajadorForm, UserForm, Comentario


# Create your views here.


def index(request):
    trabajadores = Trabajador.objects.all()
    tipos_de_servicios = TiposDeServicio.objects.all()
    form_trabajador = TrabajadorForm(request.POST)
    form_usuario = UserForm(request.POST)

    context = {'trabajadores': trabajadores,
               'tipos_de_servicios': tipos_de_servicios,
               'form_trabajador': form_trabajador,
               'form_usuario': form_usuario,
               'base_url': settings.STATIC_URL}

    my_user = auth.get_user(request)

    if my_user.is_authenticated:
        context['user_name'] = trabajadores.filter(usuarioId=my_user).first().nombre

    return render(request, 'buscoayuda/index.html', context)


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username, password=password)
        user.first_name = request.POST.get('nombre')
        user.last_name = request.POST.get('apellidos')
        user.email = request.POST.get('correo')
        user.save()

        nuevo_trabajador = Trabajador(nombre=request.POST['nombre'],
                                      apellidos=request.POST['apellidos'],
                                      aniosExperiencia=request.POST.get(
                                          'aniosExperiencia'),
                                      tiposDeServicio=TiposDeServicio.objects.get(
                                          pk=request.POST.get('tiposDeServicio')),
                                      telefono=request.POST.get('telefono'),
                                      correo=request.POST.get('correo'),
                                      imagen=request.FILES['imagen'],
                                      usuarioId=user
                                      )
        nuevo_trabajador.save()

    return HttpResponseRedirect('/')


def detalle_trabajador(request):
    return render(request, "buscoayuda/detalle.html")


def update_user_view(request):

    if request.method == 'POST':
        form_trabajador = TrabajadorForm(request.POST, request.FILES)

        if form_trabajador.is_valid():
            cleaned_data_trabajador = form_trabajador.cleaned_data
            nombre = cleaned_data_trabajador.get('nombre')
            apellidos = cleaned_data_trabajador.get('apellidos')
            aniosExperiencia = cleaned_data_trabajador.get('aniosExperiencia')
            tiposDeServicio = cleaned_data_trabajador.get('tiposDeServicio')
            telefono = cleaned_data_trabajador.get('telefono')
            correo = cleaned_data_trabajador.get('correo')
            imagen = cleaned_data_trabajador.get('imagen')

            user_model = User.objects.get(username=request.user.username,
                                          password=request.user.password)

            app_user_model = Trabajador.objects.get(usuarioId=user_model)
            app_user_model.nombre = nombre
            app_user_model.apellidos = apellidos
            app_user_model.aniosExperiencia = aniosExperiencia
            app_user_model.tiposDeServicio = tiposDeServicio
            app_user_model.telefono = telefono
            app_user_model.correo = correo
            app_user_model.imagen = imagen
            app_user_model.save()
        return HttpResponseRedirect('/')

    else:
        form_trabajador = TrabajadorForm()
        app_user_model = Trabajador.objects.filter(usuarioId_id=request.user.id).first()
        form_trabajador.fields["nombre"].initial = app_user_model.nombre
        form_trabajador.fields["apellidos"].initial = app_user_model.apellidos
        form_trabajador.fields["aniosExperiencia"].initial = app_user_model.aniosExperiencia
        form_trabajador.fields["tiposDeServicio"].initial = app_user_model.tiposDeServicio
        form_trabajador.fields["telefono"].initial = app_user_model.telefono
        form_trabajador.fields["correo"].initial = app_user_model.correo
        form_trabajador.fields["imagen"].initial = app_user_model.imagen

        context = {
            'form_trabajador': form_trabajador
        }
        return render(request, 'buscoayuda/updateTrabajador.html', context)


def detail(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    return HttpResponse(serializers.serialize("json", [trabajador]))


def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        messages.success(request, "Bienvenido al sistema {}".format(
            username), extra_tags="alert-success")
        return HttpResponseRedirect('/')
    else:
        messages.error(
            request, "?El usuario o la contrase?a son incorrectos!", extra_tags="alert-danger")
        return HttpResponseRedirect('/')


@csrf_exempt
def add_comment(request):
    if request.method == 'POST':
        new_comment = Comentario(texto=request.POST.get('texto'),
                                 trabajador=Trabajador.objects.get(
                                     pk=request.POST.get('trabajador')),
                                 correo=request.POST.get('correo'))
        new_comment.save()
    return HttpResponse(serializers.serialize("json", [new_comment]))


@csrf_exempt
def mostrarComentarios(request, idTrabajador):
    lista_comentarios = Comentario.objects.filter(
        trabajador=Trabajador.objects.get(pk=idTrabajador))

    return HttpResponse(serializers.serialize("json", lista_comentarios))
