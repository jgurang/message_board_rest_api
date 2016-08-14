from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from board.models import Message, Thread
from django.contrib.auth.models import User
from .serializers import ThreadSerializer, MessageSerializer
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

#user tests copied from https://github.com/erkarl/django-rest-framework-oauth2-provider-example/blob/master/apps/users/tests.py
#####User Tests#########
class ReadUserTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mike")

    def test_can_read_user_list(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_user_detail(self):
        response = self.client.get(reverse('user-detail', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

#####Thread Tests#########
class CreateThreadTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('admin', 'admin@admin.com', 'password123')
        self.client.login(username='admin', password='password123')
        self.data = {"title":"Test Thread 1","messages":[]}

    def test_can_create_thread(self):
        response = self.client.post(reverse('thread-list'), self.data)
        #print(response, reverse('thread-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ReadThreadTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword') #dummy user: no access priviledges
        self.client.login(username='john', password='johnpassword')
        self.thread = Thread.objects.create(title="mike",owner=self.superuser)

    def test_can_read_thread_list(self):
        response = self.client.get(reverse('thread-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_thread_detail(self):
        response = self.client.get(reverse('thread-detail', args=[self.thread.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateThreadTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.thread = Thread.objects.create(title="mike",owner=self.superuser)
        self.data = ThreadSerializer(self.thread).data
        self.data.update({'title': 'Changed'})

    def test_can_update_thread(self):
        response = self.client.put(reverse('thread-detail', args=[self.thread.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteThreadTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.thread = Thread.objects.create(title="mike",owner=self.superuser)

    def test_can_delete_thread(self):
        response = self.client.delete(reverse('thread-detail', args=[self.thread.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#####Message Tests########
class CreateMessageTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('admin', 'admin@admin.com', 'password123')
        self.client.login(username='admin', password='password123')
        self.thread = Thread.objects.create(title="mike",owner=self.superuser)
        self.threadData = ThreadSerializer(self.thread).data
        self.data = {"title":"Test Message",'thread':reverse('thread-detail', args=[self.thread.id]),"body_text":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"}

    def test_can_create_message(self):
        response = self.client.post(reverse('message-list'), self.data)
        #print(response, reverse('message-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadMessageTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.thread = Thread.objects.create(title="mike",owner=self.superuser)
        self.message = Message.objects.create(owner=self.superuser,title="Test Message", thread=self.thread, body_text="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum")


    def test_can_read_message_list(self):
        response = self.client.get(reverse('message-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_message_detail(self):
        response = self.client.get(reverse('message-detail', args=[self.message.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateMessageTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.thread = Thread.objects.create(title="mike",owner=self.superuser)
        self.message = Message.objects.create(owner=self.superuser,title="Test Message", thread=self.thread, body_text="e and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum")
        factory = APIRequestFactory()
        request = factory.get('/')
        self.data = MessageSerializer(self.message,context={'request': Request(request)}).data
        self.data.update({'title': 'Changed'})

    def test_can_update_message(self):
        response = self.client.put(reverse('thread-detail', args=[self.message.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteMessageTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.thread = Thread.objects.create(title="mike",owner=self.superuser)
        self.message = Message.objects.create(owner=self.superuser,title="Test Message", thread=self.thread, body_text="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum")

    def test_can_delete_message(self):
        response = self.client.delete(reverse('message-detail', args=[self.message.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)