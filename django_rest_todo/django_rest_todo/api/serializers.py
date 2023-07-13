from .models import Todo
from rest_framework.serializers import HyperlinkedModelSerializer

class TodoSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','title')