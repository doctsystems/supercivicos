from django.http import QueryDict
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import RateSerializer
from .models import Rate


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all().order_by('stars')
    serializer_class = RateSerializer

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            qdict = QueryDict('', mutable=True)
            qdict.update(request.data)
            qdict['is_anonymous'] = True
            name = qdict
            serializer = self.get_serializer(data=name)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

        else:
            name = request.data
            serializer = self.get_serializer(data=name)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)




