from django.shortcuts import render
from ..serilizers import RegSerilizers
# Create your views here.
from rest_framework import generics, status
import requests
import json
from errormessage import Errormessage
from rest_framework.response import Response


class RegPost(generics.GenericAPIView):
    serializer_class = RegSerilizers


    def post(self,request):
        try:
            ser = self.get_serializer(data = request.data)
            if ser.is_valid(raise_exception=True):
                a = ser.save()

                response_data = {
                                "message": "Successfull",
                                "Result" : RegSerilizers(a).data,
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

