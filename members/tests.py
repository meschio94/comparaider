from django.test import TestCase
from django.db import IntegrityError
from django.urls import reverse
from .models import User

class UserTest (TestCase):
    def setUp(self):
        User.objects.create_user(username="prova1", email="p1@email.it",device="aaaaaaaaaaaa1", password="cadabra1", is_person=True)

        User.objects.create_user(username="prova2", email="p2@email.it", device="aaaaaaaaaaaa2", password="cadabra2", is_person=True)

        User.objects.create_user(username="prova3", email="p3@email.it", device="aaaaaaaaaaaa3", password="cadabra3",
                                 is_person=True)

        User.objects.create_user(username="prova4", email="p4@email.it", device="aaaaaaaaaaaa4", password="cadabra4",
                                 is_person=True)

    def test_setup_users(self):
        self.assertEqual(User.objects.all().count(), 4)

    def test_create_existing_user(self):
        with self.assertRaises(IntegrityError) as e:
            User.objects.create_user(username="prova1", email="p1@email.it",device="aaaaaaaaaaaa1",is_person=True)
        self.assertEqual(IntegrityError, type(e.exception))

    def test_create_user(self):
        response = self.client.post(reverse('members:signup'), {
            'username': 'testcreate',
            'email' : 'testcreate@email.com',
            'is_person': True
        })
        self.assertEqual(response.status_code,200)

    def test_user_login(self):
        response = self.client.login(
            username='prova1',
            password='cadabra1'
        )
        self.assertTrue(response)

    def test_user_failed_login(self):
        response = self.client.login(
            username='prova1',
            password='error'
        )
        self.assertFalse(response)