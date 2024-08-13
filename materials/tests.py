from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Lesson, Course, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="admin@example.com")
        self.lesson = Lesson.objects.create(
            title="Test", description="Test description", owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("materials:lesson_detail", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.lesson.title)

    def test_lesson_create(self):
        url = reverse("materials:lesson_create")
        data = {
            "title": "Test",
            "description": "Test description",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("materials:lesson_update", args=(self.lesson.pk,))
        data = {
            "title": "Test update",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Test update")

    def test_lesson_delete(self):
        url = reverse("materials:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("materials:lesson_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Lesson.objects.all().count(), 1)


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="apitest@apitest.com")
        self.course = Course.objects.create(
            title="Test Course", description="Test Course", owner=self.user
        )
        self.subscription = Subscription.objects.create(
            user=self.user, course=self.course
        )
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        url = reverse("materials:course_subscribe")
        data = {
            "user": self.user.pk,
            "course": self.course.pk,
        }
        response = self.client.post(url, data)
        response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"message": "Подписка отключена"})
