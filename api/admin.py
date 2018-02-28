from django.contrib import admin
from models import Greeting
from model.question_set import QuestionSet, Question, Option

# Register your models here.


admin.site.register(Greeting)
admin.site.register(QuestionSet)
admin.site.register(Question)
admin.site.register(Option)
