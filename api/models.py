from __future__ import unicode_literals
from django.db import models
from djangae import fields


class QuestionSet(models.Model):
    QUESTION_SET_TYPES = (('Q', 'QUIZ'), ('F', 'FEEDBACK'))
    title = models.CharField('Title', max_length=160)
    desc = models.TextField('Description', max_length=400)
    image = models.URLField('Image URL', max_length=400, default='')
    type = models.CharField('Type', choices=QUESTION_SET_TYPES, max_length=1)

    def __str__(self):
        return self.title


class Question(models.Model):
    IMAGE_ORDER = (('F', 'FIRST'), ('L', 'LAST'))
    QUESTION_TYPES = (('O', 'OBJECTIVE'), ('YN', 'YES_NO'))
    desc = models.TextField('Question description', max_length=400, default='')
    image = models.URLField('Image URL', max_length=400)
    image_order = models.CharField('Image order to display', choices=IMAGE_ORDER, max_length=1)
    point = models.IntegerField('Question points')
    question_set = models.ForeignKey(QuestionSet,related_name='questions_set')

    def __str__(self):
        return self.desc


class Option(models.Model):
    OPTION_TYPES = (('T', 'TEXT'), ('I', 'IMAGE'), ('V', 'VIDEO'))
    type = models.CharField(max_length=1, choices=OPTION_TYPES)
    text = models.CharField(max_length=160)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question,related_name='options_set')

    def __str__(self):
        return self.text
