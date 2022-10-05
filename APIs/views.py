from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from symbol import dotted_as_name
from .serializers import DnsSerializer
from .models import DnsRecords
import socket
from rest_framework.parsers import MultiPartParser, FormParser


class RecordView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        file_serializer = DnsSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,domain=None):
        domain = DnsRecords.objects.get(domain=domain)
        if(request.method == 'GET'):
            if(domain):
                records = DnsRecords.objects.all()
                serializer = DnsSerializer(records, many=True)
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK) 
            else:
                ip = socket.gethostbyname(domain)
                
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
    # def get(self, request):
    #     if(request.method == 'GET'):
    #         # r = DnsRecords.objects.all().values().order_by('domain')
    #         domain = DnsRecords.objects.filter("domain")
    #         ip = DnsRecords.objects.filter("ip")
    #         ip = socket.gethostbyname(domain)
    #         try:
    #             res = {"ip":ip}
    #             return Response({"domain":domain,
    #                             "response": 
    #                                     {"success": True,
    #                                     "data":res
    #                                         }
    #                                     }) 
    #         except Exception as e:
    #             return Response({"response": f"{domain} doesn't exist"})
    #     else:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

