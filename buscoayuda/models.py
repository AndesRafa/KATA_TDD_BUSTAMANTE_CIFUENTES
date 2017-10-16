from django.contrib.auth.forms import forms
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


# MODEL CLASSES


class TiposDeServicio(models.Model):
    nombre = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='services')

    def __unicode__(self):
        return u'{0}'.format(self.nombre)

    def __str__(self):
        return u'{0}'.format(self.nombre)


class Trabajador(models.Model):
    nombre = models.CharField(max_length=1000)
    apellidos = models.CharField(max_length=1000)
    aniosExperiencia = models.IntegerField()
    tiposDeServicio = models.ForeignKey(TiposDeServicio, null=True)
    telefono = models.CharField(max_length=1000)
    correo = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='photos')
    usuarioId = models.OneToOneField(User, null=True)


# MODEL forms


class TrabajadorForm(ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Ingrese sus nombres'})
    )
    apellidos = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Ingrese sus apellidos'})
    )
    aniosExperiencia = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Cantidad de a?os de experiencia'}),
        label='A?os De Experiencia'
    )

    tiposDeServicio = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=TiposDeServicio.objects.all(),
        empty_label='Seleccione el tipo de servicio que ofrecer?',
        label='Tipo De Servicio'
    )
    telefono = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'placeholder': 'N?mero telef?nico'}),
        label='Tel?fono'
    )
    correo = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'Correo electr?nico'}),
        label='Correo'
    )

    class Meta:
        model = Trabajador
        fields = ['nombre', 'apellidos', 'aniosExperiencia','tiposDeServicio', 'telefono', 'correo', 'imagen']


class UserForm(ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Usuario'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Contrase?a'
    )

    # Create your models here.
    class Meta:
        model = User
        fields = ['username', 'password']
