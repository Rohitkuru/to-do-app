from django.test import TestCase
from ..models import Task
from datetime import datetime

# Create your tests here.


class TaskDbTest(TestCase):

    def setUp(self):
        obj = Task(title="TaskName",complete=False,created=datetime.now())
        obj.save()

    def test_db_object_return_value(self):
        name = Task.objects.get(title="TaskName")
        self.assertEquals(name.__str__(),"TaskName")

