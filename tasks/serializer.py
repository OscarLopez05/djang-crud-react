from rest_framework import serializers
from .models import Task

#El serializador se encarga de convertir los tipos de datos de django a json
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        #fields = ('id', 'title', 'description')
        fields = '__all__'