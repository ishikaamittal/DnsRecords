from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import DnsSerializer
from .models import DnsRecords
import socket
from rest_framework.parsers import MultiPartParser, FormParser


class RecordView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    # def post(self, request, *args, **kwargs):
        # if(request.method == 'POST'):
        #     domain_name = DnsRecords.objects.all().first()
        #     try:
        #         ip = socket.gethostbyname(domain_name)
        #         res= {"ip": ip}
        #         return Response({"response": 
        #                                 {"success": True,
        #                                 "data":res
        #                                     }
        #                                 }) 
        #     except Exception as e:
        #         return Response({"response": f"{domain_name} doesn't exist"})
        #             # print(f"{domain_name} doesn't exist")
        # else:
        #     return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        if(request.method == 'GET'):
            r = DnsRecords.objects.all().values().order_by('domain')
            rlist = list(r)
            try:
                res = {"ip": rlist[0]["ip"]}
                return Response({"domain":rlist[0]['domain'],
                                "response": 
                                        {"success": True,
                                        "data":res
                                            }
                                        }) 
            except Exception as e:
                return Response({"response": f"{rlist[0]['domain']} doesn't exist"})
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
