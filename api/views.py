from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from models import QuestionSet, Question
from serializers import QuestionSetSerializer, QuestionSerializer
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
import logging


class QuestionSetList(ListCreateAPIView):
    queryset = QuestionSet.objects.all()
    serializer_class = QuestionSetSerializer


class QuerySetDetail(RetrieveAPIView):
    queryset = QuestionSet.objects.all()
    serializer_class = QuestionSetSerializer


class QuestionsList(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


def index(request):
    return HttpResponse("Hello World")


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'question-sets': reverse('question_set_list',request=request, format=format)
    })
