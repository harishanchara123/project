from rest_framework import serializers
from .models import Advisor,Book

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ('AdvisorId',
                  'AdvisorName',
                  'image')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('Id',
                  'Name',
                  'Departmet',
                  'DateOfJoining',
                  'image')