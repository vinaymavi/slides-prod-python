from rest_framework.serializers import ModelSerializer
from models import QuestionSet,Question


class QuestionSetSerializer(ModelSerializer):
    class Meta:
        model = QuestionSet
        fields = ('id','title', 'desc', 'image', 'type')

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'desc', 'image','image_order', 'point','question_set')
