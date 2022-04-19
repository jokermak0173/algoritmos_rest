import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import MyTokenObtainPairSerializer, RequestSerializer
from apps.request.algorithms.avis.Controllers.datesTimesController import searchDatesTimes, searchDateTime, searchDate, searchTime

from apps.request.models import Request

ERROR_RESPONSE = ()

class DatesTimesAlgorithm(APIView):
    def post(self, request, algoritmo):
        
        user = request.user
        frase = request.data.get('frase', None)
        conv_id = request.META.get('HTTP_CONVID', None)
        site_id = request.META.get('HTTP_SITEID', None)
        bot_name = request.META.get('HTTP_BOTNAME', None)
        dataDict = {"frase_enviada": frase, "conversation_id": conv_id, "site_id": site_id, "bot_name": bot_name}
        serializer = RequestSerializer(data=dataDict)
        if serializer.is_valid():
            resp = ""
            if algoritmo == "search-dates-times":
                resp = searchDatesTimes(frase)
            elif algoritmo == "search-date-time":
                resp = searchDateTime(frase)
            elif algoritmo == "search-date":
                resp = searchDate(frase)
            elif algoritmo == "search-time":
                resp = searchTime(frase)
            else:
                return Response({'message': 'Ruta invalida'}, status=status.HTTP_404_NOT_FOUND)
            
            rq = Request(frase_enviada=frase, user=user, response=resp, response_status=status.HTTP_200_OK, conversation_id=conv_id, algorithm=algoritmo, site_id=site_id, bot_name=bot_name)
            rq.save()
            return Response({'frase_procesada': resp}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #resp = searchDatesTimes(frase)
        #return Response({'body': resp}, status.HTTP_200_OK)
"""
class DateTimeAlgorithm(APIView):
    def post(self, request):
        frase = request.data.get('frase', None)
        if not frase:
            return Response({'error': 'Es obligatorio mandar una frase para procesarla'}, status.HTTP_400_BAD_REQUEST)
        
        resp = searchDateTime(frase)
        return Response({'body': resp}, status.HTTP_200_OK)

class DateAlgorithm(APIView):
    def post(self, request):
        frase = request.data.get('frase', None)
        if not frase:
            return Response({'error': 'Es obligatorio mandar una frase para procesarla'}, status.HTTP_400_BAD_REQUEST)
        
        resp = searchDate(frase)
        return Response({'body': resp}, status.HTTP_200_OK)

class TimeAlgorithm(APIView):
    def post(self, request):
        frase = request.data.get('frase', None)
        if not frase:
            return Response({'error': 'Es obligatorio mandar una frase para procesarla'}, status.HTTP_400_BAD_REQUEST)
        
        resp = searchTime(frase)
        return Response({'body': resp}, status.HTTP_200_OK)
"""



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer