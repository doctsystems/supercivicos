from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from decouple import config
from .serializers import CreateUserSerializer
from .serializers import updatepin
#To send an email
from empresas.utils import *

import requests, random, string

CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')
HOST = config('HOST')


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    '''
    Registers user to the server. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    '''
    # Put the data from the request into the serializer
    serializer = CreateUserSerializer(data=request.data)
    # Validate the data
    if serializer.is_valid():
        # If it is valid, save the data (creates a user).
        serializer.save()
        # Then we get a token for the created user.
        # This could be done differentley
        r = requests.post('http://' + HOST + ':8000/o/token/',
            data={
                'grant_type': 'password',
                'username': request.data['username'],
                'password': request.data['password'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )
        return Response(r.json())
    return Response(serializer.errors)


#Update temporary PIN (user password)
@api_view(['POST'])
@permission_classes([AllowAny])
def update_pin(request):
    caracteres = string.ascii_letters + string.digits 
    pwd = "".join([caracteres[random.randrange(len(caracteres))] for x in range(4)])

    #Try to update the password from an existing user
    try:
        updatepin(request.data['email'], pwd)

    #If the user does not exist
    except:
        r = requests.post(
                'http://' + HOST + ':8000/authentication/register/',
                data={
                    'username': request.data['email'],
                    'password': pwd,
                    },
        )
    
    #Sending an email with the pin
    try:
        email_body = 'Hola '+ request.data['email'] + '\n\n' + 'Tu PIN de acceso es: ' + pwd + '\n\n'
        data = {'email_body': email_body, 'to_email': request.data['email'],
                            'email_subject': 'Supercívicos app: PIN de acceso'}
        Util.send_email(data)
    except Exception as e:
        return Response(str(e))

    return Response("Email enviado")


@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    '''
    Gets tokens with username and password. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    '''
    r = requests.post(
    'http://' + HOST + ':8000/o/token/',
        data={
            'grant_type': 'password',
            'username': request.data['username'],
            'password': request.data['password'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    '''
    Registers user to the server. Input should be in the format:
    {"refresh_token": "<token>"}
    '''
    r = requests.post(
    'http://' + HOST + ':8000/o/token/',
        data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    '''
    Method to revoke tokens.
    {"token": "<token>"}
    '''
    r = requests.post(
        'http://' + HOST + ':8000/o/revoke_token/',
        data={
            'token': request.data['token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    # If it goes well return sucess message (would be empty otherwise)
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)
    # Return the error if it goes badly
    return Response(r.json(), r.status_code)
