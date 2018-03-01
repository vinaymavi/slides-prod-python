from rest_framework.serializers import ModelSerializer
from models import QuestionSet


class QuestionSetSerializer(ModelSerializer):
    class Meta:
        model = QuestionSet
        fields = ('title', 'desc', 'image', 'type')
