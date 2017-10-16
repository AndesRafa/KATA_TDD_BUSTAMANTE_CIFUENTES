from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register', views.register),
    url(r'^trabajador/(?P<pk>\d+)$', views.detail),
    url(r'^detail', views.detalle_trabajador),
    url(r'^login$', views.login),
    url(r'^actualizar-usuario/$', views.update_user_view, name='updateUser'),
    url(r'^addComment/', views.add_comment),
    url(r'^mostrarComentarios/(?P<idTrabajador>\d+)$', views.mostrarComentarios),
]
