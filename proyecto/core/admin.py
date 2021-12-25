from django.contrib import admin
from .models import article

# Register your models here.
class articleAdmin(admin.ModelAdmin):
    list_display =['categoria','segmento','producto','nombreArticulo','descripcion','descripcionAll','fechaRecibido','NombreArchivoPDF','fotoNombreImagen','fechaPublicacion','estado','autor','enlace','sabiasQue','objetivoGeneral','objetivoEspecifico','tipoEstudio','metodologia','tamañoMuestra','ciudades','fechaCampo','conclusiones','agencia','accionesLogros','valorUnitario','valorTotal']
    search_fields=['nombreArticulo', 'producto']
    list_filter =['categoria']
    list_per_page= 10

admin.site.register(article,articleAdmin)