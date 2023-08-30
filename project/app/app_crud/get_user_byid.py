from ..serilizers import GetRegSerilizers
from rest_framework import generics
from ..models import RegModel
from rest_framework import status
from rest_framework.response import Response
from errormessage import Errormessage


class GetReg(generics.GenericAPIView):
    serializer_class = GetRegSerilizers

    def get(self,*args,userid):
        try:
            if RegModel.objects.get(id=userid):
                userdetails =  RegModel.objects.get(id=userid)
                serializer = GetRegSerilizers(userdetails)

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


