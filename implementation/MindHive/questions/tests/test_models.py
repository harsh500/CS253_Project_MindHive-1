from django.test import TestCase
from questions.models import Question
from ckeditor.fields import RichTextField
from users.models import User
from datetime import datetime
from tags.models import Tag
import pytz
class QuestionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        text_content=RichTextField("So I have a question")
        user1 = User.objects.create(email="example@iitk.ac.in", username="eg", password="example")
        user2 = User.objects.create(email="example2@iitk.ac.in", username="eg2", password="example2")
        tag=Tag.objects.create(name="tag1")
        User.objects.create(email="example@example.com", username="eg", password="example")
        question=Question.objects.create(text=text_content, author=user1, anonymous=False, pub_date=datetime(2020,1,1,0,0,0,tzinfo=pytz.UTC),title="How to do this?")
        question=Question.objects.create(text=text_content, author=user2, anonymous=False, pub_date=datetime(2020,1,1,0,0,0,tzinfo=pytz.UTC),title="How to do this?")
        question.likedBy.add(user1)
        question.dislikedBy.add(user2)
        question.viewedBy.add(user1)
        question.tags.add(tag)
        question.save()
    def test_title_max_length(self):
        question = Question.objects.get(id=1)
        max_length = question._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_question_name(self):
        question = Question.objects.get(id=1)
        expected_object_name = question.title
        self.assertEqual(str(question), expected_object_name)

    def test_content_richfield(self):
        question = Question.objects.get(id=1)
        expected_object_name = question.text
        self.assertEqual(str(RichTextField("So I have a question")), expected_object_name)
    
    def test_tag_check(self):
        question = Question.objects.get(id=1)
        expected_object_name = question.tags.get(id=1).name
        self.assertEqual("tag1", expected_object_name)

    def test_likedBy_check(self):
        question = Question.objects.get(id=1)
        expected_object_name = question.likedBy.get(id=1).username
        self.assertEqual("eg", expected_object_name)

    def test_dislikedBy_check(self):
        question = Question.objects.get(id=1)
        expected_object_name = question.dislikedBy.get(id=2).username
        self.assertEqual("eg2", expected_object_name)

    def test_viewedby_check(self):
        question = Question.objects.get(id=1)
        expected_object_name = question.viewedBy.get(id=1).username
        self.assertEqual("eg", expected_object_name)
    
    def test_viewedby_check(self):
        question = Question.objects.get(id=1)
        expected_object_name = question.viewedBy.get(id=1).username
        self.assertEqual("eg", expected_object_name)
    
    def test_check_pubdate(self):
        question = Question.objects.get(id=1)
        expected_object_name = question.pub_date
        self.assertEqual(expected_object_name, datetime(2020,1,1,0,0,0,tzinfo=pytz.UTC))

    def test_check_author(self):
        question = Question.objects.get(id=1)
        expected_object_name = question.author.username
        self.assertEqual("eg", expected_object_name)