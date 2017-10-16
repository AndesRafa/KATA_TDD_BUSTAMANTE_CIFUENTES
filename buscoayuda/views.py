from django.shortcuts import render

# Create your views here.
def index(request):
    # trabajadores = Trabajador.objects.all()
    # tipos_de_servicios = TiposDeServicio.objects.all()
    # form_trabajador = TrabajadorForm(request.POST)
    # form_usuario = UserForm(request.POST)

    # context = {'trabajadores': trabajadores, 'tipos_de_servicios': tipos_de_servicios,
    #            'form_trabajador': form_trabajador, 'form_usuario': form_usuario, 'base_url': settings.STATIC_URL}
    # return render(request, 'buscoayuda/index.html', context)
    return render(request, 'buscoayuda/index.html', None)
