from rest_framework import serializers
from django.contrib.auth.models import User

class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

#    def updatepin(validated_data user_email, pwd):
#        users = User.objects.filter(email='<'+ user_email + '>')
#        user = users[0]
#        user.set_password(pwd)
#        user.save()

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

def updatepin(usuario,pwd):
    u = User.objects.get(username=usuario)
    u.set_password(pwd)
    u.save()
