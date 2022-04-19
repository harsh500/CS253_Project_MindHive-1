from django import forms, setup
from django.test import TestCase
from matplotlib import widgets
from questions.models import Question
from notifications.models import Notification
from questions.forms import CreateQuestionForm
from questions.forms import AddAnswerForm
from questions.forms import CreateReportForm
from users.models import User
from tags.models import Tag
from answers.models import Answer
from comments.models import Comment
from ckeditor.fields import RichTextField
from datetime import datetime
import pytz
# class Setup_Class(TestCase):
    # def setUp(self):
        # self.user = User.objects.create(email="user@iitk.ac.in", username="user", password="cscbndm",name="user")
        # user1 = User(email="example@iitk.ac.in", username="eg", password="example",name="harish")
        # user1.save()
        # tag = Tag.objects.create(name="Anarchy")

        # question = Question.objects.create(title='test',tags='Anarchy')

class QuestionFormTest(TestCase):
    def test_valid(self):
        user = User.objects.create(email="user@iitk.ac.in", username="user", password="cscbndm",name="user")
        tag = Tag.objects.create(name="Anarchy")
        # forms.CheckboxSelectMultiple
        form_data = {'title': "user",
                     'text': "Usertext",
                     'tags': ['1'],
                     'author': user,
                     'anonymous':False}
        form = CreateQuestionForm(data = form_data)
        self.assertTrue(form.is_valid())
        saved = form.save()
        self.assertEqual(saved.title, "user")
        self.assertEqual(saved.text, "Usertext")
        # self.assertEqual(saved.tags, tag)
        self.assertEqual(saved.author, user)

class AnswerFormTest(TestCase):
    def test_valid(self):
        user = User.objects.create(email="user@iitk.ac.in", username="user", password="cscbndm",name="user")
        tag = Tag.objects.create(name="Anarchy")
        question = Question.objects.create(title='test',author=user)
        question.tags.set([tag])
        form_data = {'text': 'Usertext',
                     'author': user,
                     'anonymous':False,
                     'to_question': question}
                     
        form = AddAnswerForm(data = form_data)
        self.assertTrue(form.is_valid())
        saved = form.save()
        self.assertEqual(saved.text, "Usertext")
        # self.assertEqual(saved.tags, "Anarchy")
        # self.assertEqual(saved.author, user)
        # self.assertEqual(saved.timestamp.date(),datetime.now().date())


# Not Working
class ReportFormTest(TestCase):
    def test_valid(self):
        user = User.objects.create(email="user@iitk.ac.in", username="user", password="cscbndm",name="user")
        user1 = User.objects.create(email="example@iitk.ac.in", username="eg", password="example",name="harish")
        tag = Tag.objects.create(name="Anarchy")
        question = Question.objects.create(title='test',author=user)
        question.tags.set([tag])
        # answer = Answer.objects.create(text='Usertext',author=user,to_question=question)
        # comment = Comment.objects.create(text='Usertext',author=user)
        form_data = {'report_text': 'Usertext',
                     'reporter': user,
                     'reported_user': user1,
                     'reportedObjType': 'q',
                     'reportedObjQ': question,
                     'reportedObjA': None,
                     'reportedObjC': None}
        form = CreateReportForm(data = form_data)
        self.assertTrue(form.is_valid())
        saved = form.save()
        self.assertEqual(saved.report_text, "Usertext")
