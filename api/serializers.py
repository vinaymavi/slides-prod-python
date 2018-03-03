from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from models import QuestionSet, Question, Option


class OptionSerializer(ModelSerializer):
    class Meta:
        model = Option
        fields = ('id', 'type', 'text', 'is_correct', 'question')


class QuestionSerializer(HyperlinkedModelSerializer):
    options_set = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'desc', 'image', 'image_order', 'point', 'question_set','options_set')
        extra_kwargs = {
            'url': {'view_name': 'questionset-detail', 'lookup_field': 'question_set'}
        }


class QuestionSetSerializer(ModelSerializer):
    questions_set = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = QuestionSet
        fields = ('id', 'title', 'desc', 'image', 'type', 'questions_set')
