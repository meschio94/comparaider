from django.test import TestCase
from django.urls import reverse, reverse_lazy
from members.models import User
from showcase.models import Maker, Glider, Size
from .models import CompareItems, SizeItem


class CompareToolTest(TestCase):

    def setUp(self):
        User.objects.create_user(username="prova1", email="p1@email.it", device="aaaaaaaaaaaa1", password="cadabra1",
                                 is_person=True)

        Maker.objects.create(name="Produttore1", logoImage=None, textIntro="prova", account=None)
        Maker.objects.create(name="Produttore2", logoImage=None, textIntro="prova", account=None)
        Maker.objects.create(name="Produttore3", logoImage=None, textIntro="prova", account=None)
        Maker.objects.create(name="Produttore4", logoImage=None, textIntro="prova", account=None)

        Glider.objects.create(name="vela1P1", maker=Maker.objects.get(pk=1), year=2021, gliderImage=None)
        Glider.objects.create(name="vela1P2", maker=Maker.objects.get(pk=2), year=2021, gliderImage=None)
        Glider.objects.create(name="vela1P3", maker=Maker.objects.get(pk=3), year=2021, gliderImage=None)
        Glider.objects.create(name="vela1P4", maker=Maker.objects.get(pk=4), year=2021, gliderImage=None)

        Size.objects.create(glider=1, certification='A', size='S', takeoffWeightMin=20, takeoffWeightMax=30,
                            gliderWeight=5, flatArea=10, projectArea=15, cells=9)
        Size.objects.create(glider=1, certification='A', size='M', takeoffWeightMin=20, takeoffWeightMax=30,
                            gliderWeight=5, flatArea=10, projectArea=15, cells=9)
        Size.objects.create(glider=1, certification='A', size='L', takeoffWeightMin=20, takeoffWeightMax=30,
                            gliderWeight=5, flatArea=10, projectArea=15, cells=9)

        Size.objects.create(glider=2, certification='B', size='S', takeoffWeightMin=20, takeoffWeightMax=30,
                            gliderWeight=5, flatArea=10, projectArea=15, cells=9)
        Size.objects.create(glider=2, certification='B', size='M', takeoffWeightMin=20, takeoffWeightMax=30,
                            gliderWeight=5, flatArea=10, projectArea=15, cells=9)
        Size.objects.create(glider=2, certification='B', size='L', takeoffWeightMin=20, takeoffWeightMax=30,
                            gliderWeight=5, flatArea=10, projectArea=15, cells=9)

        Size.objects.create(glider=3, certification='C', size='S', takeoffWeightMin=20, takeoffWeightMax=30,
                            gliderWeight=5, flatArea=10, projectArea=15, cells=9)
        Size.objects.create(glider=3, certification='C', size='M', takeoffWeightMin=20, takeoffWeightMax=30,
                            gliderWeight=5, flatArea=10, projectArea=15, cells=9)
        Size.objects.create(glider=3, certification='C', size='L', takeoffWeightMin=20, takeoffWeightMax=30,
                            gliderWeight=5, flatArea=10, projectArea=15, cells=9)

        Size.objects.create(glider=4, certification='D', size='S', takeoffWeightMin=20, takeoffWeightMax=30,
                            gliderWeight=5, flatArea=10, projectArea=15, cells=9)
        Size.objects.create(glider=4, certification='D', size='M', takeoffWeightMin=20, takeoffWeightMax=30,
                            gliderWeight=5, flatArea=10, projectArea=15, cells=9)
        Size.objects.create(glider=41, certification='D', size='L', takeoffWeightMin=20, takeoffWeightMax=30,
                            gliderWeight=5, flatArea=10, projectArea=15, cells=9)

    #def test_add_glider(self):

