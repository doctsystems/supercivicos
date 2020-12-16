from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import StickersSerializer
from .models import Stickers


class StickersViewSet(viewsets.ModelViewSet):
    queryset = Stickers.objects.all().order_by('nombre')
    serializer_class = StickersSerializer



'''
class StickersAPIView(APIView):

    #def get(self, request,format=None):
        #stickers=Stickers.objects.all()
        #data=StickersSerializer(stickers, many=True).data
        #return Response(data)
    

    def post(self, request, format=None):
        serializer=StickersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''