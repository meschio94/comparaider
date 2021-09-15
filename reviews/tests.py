from django.test import TestCase
from django.test import TestCase
from django.db import IntegrityError
from django.urls import reverse, reverse_lazy
from members.models import User
from .models import GliderReview
from showcase.models import Maker,Glider,Size

class ReviewTest(TestCase):

    def setUp(self):
        User.objects.create_user(username="prova1", email="p1@email.it", device="aaaaaaaaaaaa1", password="cadabra1",
                                 is_person=True)

        User.objects.create_user(username="prova2", email="p2@email.it", device="aaaaaaaaaaaa2", password="cadabra2",
                                 is_person=True)

        User.objects.create_user(username="prova3", email="p3@email.it", device="aaaaaaaaaaaa3", password="cadabra3",
                                 is_person=True)

        User.objects.create_user(username="prova4", email="p4@email.it", device="aaaaaaaaaaaa4", password="cadabra4",
                                 is_person=True)

        User.objects.create_user(username="provaMaker1", email="pM1@email.it", device="aaaaaaaaaaam1", password="cadabram1",
                                 is_person=False, is_manufacturer=True)

        Maker.objects.create(name="Produttore1",logoImage=None,textIntro="prova",account=User.objects.get(pk=5))

        Glider.objects.create(name="velaP1",maker=Maker.objects.get(pk=1),year=2021,gliderImage=None)








    def test_add_review(self):
        self.client.login(
            username='prova1',
            password='cadabra1'
        )
        response = self.client.post(reverse_lazy('reviews:add_review', kwargs={'pk': 1}), {
            'content': 'good',
            'stars': 4
        })
        self.assertEqual(GliderReview.objects.filter(user=1).count(),1)


    def test_add_second_review(self):
        self.client.login(
            username='prova2',
            password='cadabra2'
        )
        response = self.client.post(reverse_lazy('reviews:add_review', kwargs={'pk': 1}), {
            'content': 'good',
            'stars': 3
        })
        self.assertEqual(GliderReview.objects.filter(user=2).count(),1)

    def test_add_double_review_forbidden(self):
        self.client.login(
            username='prova1',
            password='cadabra1'
        )
        response = self.client.post(reverse_lazy('reviews:add_review', kwargs={'pk': 1}), {
            'content': 'good',
            'stars': 4
        })
        response = self.client.post(reverse_lazy('reviews:add_review', kwargs={'pk': 1}), {
            'content': 'not',
            'stars': 1
        })
        self.assertEqual(response.status_code,403)
        self.assertEqual(GliderReview.objects.filter(user=1).count(), 1)



    def test_maker_add_review_forbidden(self):
        self.client.login(
            username='provaMaker1',
            password='cadabram1'
        )
        response = self.client.post(reverse_lazy('reviews:add_review', kwargs={'pk': 1}))
        self.assertEqual(GliderReview.objects.filter(user=5).count(), 0)
        self.assertRedirects(response, '/members/login/?next=/reviews/add_review/1/')

    def test_edit_review(self):
        self.client.login(
            username='prova1',
            password='cadabra1'
        )
        response = self.client.post(reverse_lazy('reviews:add_review', kwargs={'pk': 1}), {
            'content': 'good',
            'stars': 4
        })

        response = self.client.post(reverse_lazy('reviews:edit_review', kwargs={'pkg':1, 'pkr':1}), {
            'content': 'edit',
            'stars': 1
        })
        content = GliderReview.objects.get(user=1)
        self.assertEqual(content.content, "edit")

