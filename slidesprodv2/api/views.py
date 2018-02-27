from django.http import HttpResponse,JsonResponse
from models import Greeting
from rest_framework import routers, serializers, viewsets

class GreetingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Greeting
        fields =('number','messaage')

def index(request):
    return HttpResponse("Welcome to api page.")

def api(req):
    greetings = Greeting.objects.all()
    serializer = GreetingSerializer(greetings,many=True)
    return JsonResponse(serializer.data, safe=False);