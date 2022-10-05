from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DnsSerializer
from .models import DnsRecords
import socket
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import MultiPartParser, FormParser


class RecordView(APIView):

    def get(self,request,domain=None):
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
        
class RecordList(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def get(self, request):
        snippets = DnsRecords.objects.all()
        serializer = DnsSerializer(snippets, many=True)
        return Response(serializer.data) 

    def post(self,request):

        serializer = DnsSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)