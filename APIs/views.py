from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import DnsSerializer
from .models import DnsRecords
import socket
import json
from rest_framework.parsers import MultiPartParser, FormParser


class RecordView(APIView):
    # parser_classes = (MultiPartParser, FormParser)

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        file_serializer = DnsSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,domain=None):
        try:
            domain_name  = DnsRecords.objects.get(domain=domain)
            record = domain_name
            serializer = DnsSerializer(record)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)       
        except:
            try:
                ip = socket.gethostbyname(domain)
                r = {
                    'domain':domain,
                    'ip':ip
                    }
                r_json =  r
                return Response({"status": "success", "data": r_json}, status=status.HTTP_200_OK)
            except Exception :
                return Response({"status": f"{domain} not found"}, status=status.HTTP_400_BAD_REQUEST)