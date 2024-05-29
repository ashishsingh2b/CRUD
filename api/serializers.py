from rest_framework import serializers
from Home.models import Entry

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['ID','data1','data2']