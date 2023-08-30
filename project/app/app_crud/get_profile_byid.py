from ..serilizers import GetProfileSerilizer
from rest_framework import generics
from ..models import ProfileModel
from rest_framework import status
from rest_framework.response import Response
from errormessage import Errormessage


class GetProfile(generics.GenericAPIView):
    serializer_class = GetProfileSerilizer

    def get(self,*args,id):
        try:
            if ProfileModel.objects.get(id=id):
                profiledata =  ProfileModel.objects.get(id=id)
                serializer = GetProfileSerilizer(profiledata)

                response = {
                    'message': 'Success',
                    "Result" : serializer.data,
                    'Status' : 200,
                    'HasError' : False
                }
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                response = {
                    'message': 'There is no data for this id',
                    "Result" : False,
                    'Status' : 400,
                    'HasError' : True
                }
                return Response(response, status=status.HTTP_201_CREATED)
        except Exception as e:
            response = {
                    'message': Errormessage(e),
                    "Result" : False,
                    'Status' : 400,
                    'HasError' : True
                }
            return Response(response, status=status.HTTP_201_CREATED)


