from rest_framework import serializers
from .models import Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['id',]

class CommentSerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)
	userid = serializers.PrimaryKeyRelatedField(write_only=True, queryset = User.objects.all(), source = 'user')

	class Meta:
		model = Comment
		# fields = '__all__'
		read_only_fields = ['estado', ]
		exclude = ['estado', 'fecha_creacion', 'fecha_modificacion', 'usuario_creacion', 'usuario_modificacion']