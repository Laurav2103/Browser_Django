from django.db import models

# Create your models here.

class article(models.Model):
    #id--> numero autoincrementable
    categoria = models.CharField(max_length=80)
    segmento = models.CharField(max_length=80)
    producto = models.CharField(max_length=80)
    nombreArticulo = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=80)
    descripcionAll = models.CharField(max_length=80)
    fechaRecibido = models.CharField(max_length=80)
    NombreArchivoPDF = models.CharField(max_length=80)
    fotoNombreImagen = models.CharField(max_length=80)
    fechaPublicacion = models.CharField(max_length=80)
    estado = models.CharField(max_length=80)
    autor = models.CharField(max_length=80)
    enlace = models.CharField(max_length=80)
    sabiasQue = models.CharField(max_length=80)
    objetivoGeneral = models.CharField(max_length=80)
    objetivoEspecifico = models.CharField(max_length=80)
    tipoEstudio = models.CharField(max_length=80)
    metodologia = models.CharField(max_length=80)
    tamañoMuestra = models.CharField(max_length=80)
    ciudades = models.CharField(max_length=80)
    fechaCampo = models.CharField(max_length=80)
    conclusiones = models.CharField(max_length=80)
    agencia = models.CharField(max_length=80)
    accionesLogros = models.CharField(max_length=80)
    valorUnitario = models.CharField(max_length=80)
    valorTotal = models.CharField(max_length=80)

    