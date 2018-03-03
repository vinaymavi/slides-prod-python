from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from models import QuestionSet,Question


class QuestionSetSerializer(ModelSerializer):
    class Meta:
        model = QuestionSet
        fields = ('id','title', 'desc', 'image', 'type')

class QuestionSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'desc', 'image','image_order', 'point','question_set')
        extra_kwargs = {
            'url': {'view_name': 'questionset-detail', 'lookup_field': 'question_set'}
        }
