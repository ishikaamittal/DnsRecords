from rest_framework import serializers
from .models import DnsRecords

class DnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DnsRecords
        fields = '__all__'