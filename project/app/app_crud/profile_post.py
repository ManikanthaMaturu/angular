from django.shortcuts import render
from ..serilizers import ProfileSerilizer
# Create your views here.
from rest_framework import generics, status
import requests
import json
from errormessage import Errormessage
from rest_framework.response import Response


class ProfilePost(generics.GenericAPIView):
    serializer_class = ProfileSerilizer


    def post(self,request):
        try:
            ser = self.get_serializer(data = request.data)
            if ser.is_valid(raise_exception=True):
                ser.save()

                response_data = {
                                "message": "Successfull",
                                "Result" : True,
                                'Status' : 200,
                                'HasError' : False
                            }
                return Response(response_data, status=status.HTTP_201_CREATED)
            else:
                response_data = {
                    "message": "Fail",
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

