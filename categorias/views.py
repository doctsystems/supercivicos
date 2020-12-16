from django.shortcuts import render
from rest_framework import viewsets

from categorias.serializers import CategoriaSerializer
from categorias.models import Categoria


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by('nombre')
    serializer_class = CategoriaSerializer

    def crate(self, request, *args, **kwargs):
        pass
