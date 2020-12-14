from .models import Video, VideoLike
from .serializers import VideoSerializer, VideoLikeSerializer

from django.shortcuts import get_object_or_404

from rest_framework import viewsets, views, filters
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class VideoViewSet(viewsets.ModelViewSet):
	queryset = Video.objects.all()
	serializer_class = VideoSerializer
	filter_backends = [filters.SearchFilter, filters.OrderingFilter]
	search_fields = ['titulo']
	ordering_fields = ['likes']

class MarcarVideoLike(views.APIView):
	# authentication_classes = [TokenAuthentication]
	# permission_classes = [IsAuthenticated]

	# POST -> Se usa para crear un recurso sin un identificador
	# PUT -> Se usa para crear/reemplazar un recurso con un identificador
	def post(self, request):
		video = get_object_or_404(Video, id=self.request.data.get('id', 0))
		like, created = VideoLike.objects.get_or_create(video=video, usuario=request.user)

		# Por defecto suponemos que se crea bien
		content = {
			'id': video.id,
			'like': True
		}

		# Si no se ha creado es que ya existe, entonces borramos el favorito
		if not created:
			like.delete()
			content['like'] = False

		return Response(content)

class ListarVideosLikes(views.APIView):
	# authentication_classes = [TokenAuthentication]
	# permission_classes = [IsAuthenticated]

	# GET -> Se usa para hacer lecturas
	def get(self, request):
		videos_likes = VideoLike.objects.all()
		serializer = VideoLikeSerializer(videos_likes, many=True)
		return Response(serializer.data)

class ListarMisVideosLikes(views.APIView):
	# authentication_classes = [TokenAuthentication]
	# permission_classes = [IsAuthenticated]

	# GET -> Se usa para hacer lecturas
	def get(self, request):
		videos_likes = VideoLike.objects.filter(usuario=request.user)
		serializer = VideoLikeSerializer(videos_likes, many=True)
		return Response(serializer.data)
