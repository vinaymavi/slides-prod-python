from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from models import QuestionSet
from serializers import QuestionSetSerializer


class QuestionSetList(ListCreateAPIView):
    queryset = QuestionSet.objects.all()
    serializer_class = QuestionSetSerializer


def index(request):
    return HttpResponse("Hello World")
