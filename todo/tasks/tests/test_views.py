from django.test import TestCase
from django.urls import reverse
from ..models import Task
from datetime import datetime

class TestViews(TestCase):

    def setUp(self):

        obj = Task(title="TaskName", complete=False, created=datetime.now())
        obj.save()


        found_task = Task.objects.get(title="TaskName")

        self.update_task_url=reverse("update_task",args=[found_task.id])
        self.delete_task_url=reverse("delete",args=[found_task.id])

        self.update_task_data = {

            'title': "Modified Task title",
            "complete": True

        }

        self.delete_task_data = {
            'id': found_task.id
        }

    def test_home_page_GET(self):

        found_home = self.client.get("/")
        self.assertEqual(found_home.status_code,200)


    def test_home_page_POST(self):

        home_post = self.client.post("/",data={"title":"This is test task"})
        self.assertEqual(home_post.status_code,302)



    def test_update_task_page_GET(self):

        update_get_response = self.client.get(self.update_task_url)
        self.assertEqual(update_get_response.status_code,200)


    def test_update_task_page_POST(self):

        update_post_response = self.client.post(self.update_task_url,self.update_task_data)
        self.assertEqual(update_post_response.status_code,302)


    def test_delete_task_page_GET(self):

        delete_get_response = self.client.get(self.delete_task_url)
        self.assertEqual(delete_get_response.status_code,200)

    def test_delete_task_page_POST(self):

        delete_post_response = self.client.post(self.delete_task_url,self.delete_task_data)
        self.assertEqual(delete_post_response.status_code,302)
