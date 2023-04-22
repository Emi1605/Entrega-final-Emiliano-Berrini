
from django.contrib import admin
from django.urls import include, path
from hola_mundo.views import *
from SecondMarket.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('personas', mostrar_personas, name= "personas"),
    path('personas/create', crear_personas, name="personas-create"),
    path('personas_list', buscarpersonas.as_view(), name="personas-list"),
    path('productos', mostrar_productos, name="productos"),
    path('productos/create', crear_productos, name="productos-create"),
    path('productos_list', buscarProductos.as_view(), name="productos-list"),
    path('ventas', mostrar_ventas, name="ventas"),
    path('ventas/create', crear_ventas, name="ventas-create"),
    path('ventas/list', buscarVentas.as_view(), name="ventas-list"),
    path('post/list',PostList.as_view(),name='post-list'),
    path('post/<pk>/detail',PostDetail.as_view(),name='post-detail'),
    path('post/create',PostCreate.as_view(),name='post-create'),
    path('post/<pk>/update',PostUpdate.as_view(),name='post-update'),
    path('post/<pk>/delete',PostDelete.as_view(),name='post-delete'),
    path('signup/',SignUp.as_view(),name='signup'),
    path('login/', Login.as_view(),name='login'),
    path('logout/', Logout.as_view(),name='logout'),
    path('profile/<pk>/update',ProfileUpdate.as_view(),name='profile-update'),
    path('profile/create',ProfileCreate.as_view(),name='profile-create'),
    path('mensaje/create', MensajeCreate.as_view(),name='mensaje-create'),
    path('mensaje/<pk>/delete',MensajeDelete.as_view(),name='mensaje-delete'),
    path('mensaje/list',MensajeList.as_view(),name='mensaje-list'),
    path('aboutme', about, name="about"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)