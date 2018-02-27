from django.http import HttpResponse
from models import Greeting
from rest_framework import routers, serializers, viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class GreetingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Greeting
        fields =('number','messaage')

def index(request):
    return HttpResponse("Welcome to api page.")

@api_view(['GET', 'POST'])
def api(req):
    greetings = Greeting.objects.all()
    serializer = GreetingSerializer(greetings,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)