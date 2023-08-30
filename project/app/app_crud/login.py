from django.shortcuts import render
from ..serilizers import LoginSerializer,GetRegSerilizers
from ..models import RegModel
# Create your views here.
from rest_framework import generics, status
import requests
import json
from errormessage import Errormessage
from rest_framework.response import Response


class UserLogin(generics.GenericAPIView):
    serializer_class = LoginSerializer


    def post(self,request):
        try:
            username = request.data.get('UserName')
            password = request.data.get('Password')
            if RegModel.objects.get(UserName=username):
                data = RegModel.objects.get(UserName=username)

                if data.Password == password:

                    serializer = GetRegSerilizers(data)
                    response_data = {
                                    "message": "Successfull",
                                    "Result" : serializer.data,
                                    'Status' : 200,
                                    'HasError' : False
                                }
                    return Response(response_data, status=status.HTTP_201_CREATED)
                else:
                    response_data = {
                        "message": "Invalid Password",
                        "Result" : False,
                        'Status' : 400,
                        'HasError' : True
                    }
                    return Response(response_data, status=status.HTTP_201_CREATED)
            else:
                response_data = {
                    "message": "Invalid UserName",
                    "Result" : False,
                    'Status' : 400,
                    'HasError' : True
                }
                return Response(response_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            response_data = {
                    "message":Errormessage(e),
                    "Result" : False,
                    'Status' : 400,
                    'HasError' : True
                }
            return Response(response_data, status=status.HTTP_201_CREATED)

