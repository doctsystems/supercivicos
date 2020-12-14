from rest_framework import serializers
from .models import Video, VideoLike

class VideoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Video
		fields = ['id', 'titulo', 'video']

class VideoLikeSerializer(serializers.ModelSerializer):
	video = VideoSerializer()
	class Meta:
		model = VideoLike
		fields = ['video']