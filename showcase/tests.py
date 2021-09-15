from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy
from members.models import User
from showcase.models import Maker, Glider, Size
from django.contrib.staticfiles import finders
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile

from io import BytesIO
from PIL import Image
from django.core.files.base import File


class prova(TestCase):

    def setUp(self):
        User.objects.create_user(username="prova1m1", email="p1m1@email.it", device="aaaaaaaaaaaam1",
                                 password="cadabra1",
                                 is_person=False, is_manufacturer=True)

        User.objects.create_user(username="prova2m2", email="p2m2@email.it", device="aaaaaaaaaaaam2",
                                 password="cadabra1",
                                 is_person=False, is_manufacturer=True)

        User.objects.create_user(username="prova3m3", email="p3m3@email.it", device="aaaaaaaaaaaam3",
                                 password="cadabra1",
                                 is_person=False, is_manufacturer=True)

        User.objects.create_user(username="prova1", email="p1@email.it", device="aaaaaaaaaaaa1", password="cadabra1",
                                 is_person=True)

        Maker.objects.create(name="Produttore1", logoImage=None, textIntro="prova", account=User.objects.get(pk=1))
        Maker.objects.create(name="Produttore2", logoImage=None, textIntro="prova", account=User.objects.get(pk=2))
        Maker.objects.create(name="Produttore3", logoImage=None, textIntro="prova", account=User.objects.get(pk=3))
        Maker.objects.create(name="Produttore4", logoImage=None, textIntro="prova", account=None)

        Glider.objects.create(name="vela1P1", maker=Maker.objects.get(pk=1), year=2021, gliderImage=None)
        Glider.objects.create(name="vela1P2", maker=Maker.objects.get(pk=2), year=2021, gliderImage=None)
        Glider.objects.create(name="vela1P3", maker=Maker.objects.get(pk=3), year=2021, gliderImage=None)
        Glider.objects.create(name="vela1P4", maker=Maker.objects.get(pk=4), year=2021, gliderImage=None)

        Size.objects.create(glider=Glider.objects.get(pk=1), certification='A', size='S', takeoffWeightMin=20,
                            takeoffWeightMax=30,
                            gliderWeight=5, flatArea=10, projectArea=15, cells=9)
        Size.objects.create(glider=Glider.objects.get(pk=1), certification='A', size='M', takeoffWeightMin=20,
                            takeoffWeightMax=30,
                            gliderWeight=5, flatArea=10, projectArea=15, cells=9)
        Size.objects.create(glider=Glider.objects.get(pk=1), certification='A', size='L', takeoffWeightMin=20,
                            takeoffWeightMax=30,
                            gliderWeight=5, flatArea=10, projectArea=15, cells=9)

        Size.objects.create(glider=Glider.objects.get(pk=2), certification='B', size='S', takeoffWeightMin=20,
                            takeoffWeightMax=30,
                            gliderWeight=5, flatArea=10, projectArea=15, cells=9)
        Size.objects.create(glider=Glider.objects.get(pk=2), certification='B', size='M', takeoffWeightMin=20,
                            takeoffWeightMax=30,
                            gliderWeight=5, flatArea=10, projectArea=15, cells=9)
        Size.objects.create(glider=Glider.objects.get(pk=2), certification='B', size='L', takeoffWeightMin=20,
                            takeoffWeightMax=30,
                            gliderWeight=5, flatArea=10, projectArea=15, cells=9)

        Size.objects.create(glider=Glider.objects.get(pk=3), certification='C', size='S', takeoffWeightMin=20,
                            takeoffWeightMax=30,
                            gliderWeight=5, flatArea=10, projectArea=15, cells=9)
        Size.objects.create(glider=Glider.objects.get(pk=3), certification='C', size='M', takeoffWeightMin=20,
                            takeoffWeightMax=30,
                            gliderWeight=5, flatArea=10, projectArea=15, cells=9)
        Size.objects.create(glider=Glider.objects.get(pk=3), certification='C', size='L', takeoffWeightMin=20,
                            takeoffWeightMax=30,
                            gliderWeight=5, flatArea=10, projectArea=15, cells=9)

        Size.objects.create(glider=Glider.objects.get(pk=4), certification='D', size='S', takeoffWeightMin=20,
                            takeoffWeightMax=30,
                            gliderWeight=5, flatArea=10, projectArea=15, cells=9)
        Size.objects.create(glider=Glider.objects.get(pk=4), certification='D', size='M', takeoffWeightMin=20,
                            takeoffWeightMax=30,
                            gliderWeight=5, flatArea=10, projectArea=15, cells=9)
        Size.objects.create(glider=Glider.objects.get(pk=4), certification='D', size='L', takeoffWeightMin=20,
                            takeoffWeightMax=30,
                            gliderWeight=5, flatArea=10, projectArea=15, cells=9)

    @staticmethod
    def get_image_file(name, ext='png', size=(50, 50), color=(256, 0, 0)):
        file_obj = BytesIO()
        image = Image.new("RGBA", size=size, color=color)
        image.save(file_obj, ext)
        file_obj.seek(0)
        return File(file_obj, name=name)

    def test_add_maker_glider(self):
        self.client.login(
            username='prova1m1',
            password='cadabra1'
        )
        image = self.get_image_file('image.png')
        response = self.client.post(reverse('showcase:add_glider'), {
            'name': 'vela2P1',
            'gliderImage': image,
            'year': 2020,

        })
        self.assertEqual(Glider.objects.filter(maker_id=1).count(), 2)

    def test_remove_maker_glider(self):
        self.client.login(
            username='prova2m2',
            password='cadabra1'
        )
        response = self.client.post(reverse('showcase:remove_glider'), {
            'gliderPk': 2,

        })
        self.assertEqual(Glider.objects.filter(maker_id=2).count(), 0)

    def test_add_size_glider(self):
        self.client.login(
            username='prova1m1',
            password='cadabra1'
        )
        image = self.get_image_file('image.png')
        response = self.client.post(reverse('showcase:add_size', kwargs={'pk': 1}), {
            'certification': 'D',
            'size': 'XL',
            'takeoffWeightMin': 50,
            'takeoffWeightMax': 80,
            'gliderWeight': 5,
            'flatArea': 20,
            'projectArea': 30,
            'cells': 10

        })
        self.assertEqual(Size.objects.filter(glider_id=1).count(), 4)

    def test_remove_size_glider(self):
        self.client.login(
            username='prova1m1',
            password='cadabra1'
        )

        response = self.client.post(reverse('showcase:remove_size'), {
            'gliderPk': 1,
            'sizeId': 1,
        })
        self.assertEqual(Size.objects.filter(glider_id=1).count(), 2)

    def test_edit_size_glider(self):
        self.client.login(
            username='prova3m3',
            password='cadabra1'
        )

        response = self.client.post(reverse('showcase:edit_size', kwargs={'pkg': 3, 'pks': 8,}),{
            'certification': 'D',
            'size': 'AA',
            'takeoffWeightMin': 50,
            'takeoffWeightMax': 80,
            'gliderWeight': 5,
            'flatArea': 20,
            'projectArea': 30,
            'cells': 10
        })
        content =Size.objects.get(pk=8)
        self.assertEqual(content.certification, "D")
        self.assertEqual(content.size, "AA")
        self.assertEqual(Size.objects.filter(glider_id=3).count(), 3)

    def test_edit_other_size_glider(self):
        self.client.login(
            username='prova3m3',
            password='cadabra1'
        )

        response = self.client.post(reverse('showcase:edit_size', kwargs={'pkg': 1, 'pks': 1,}),{
            'certification': 'D',
            'size': 'AA',
            'takeoffWeightMin': 50,
            'takeoffWeightMax': 80,
            'gliderWeight': 5,
            'flatArea': 20,
            'projectArea': 30,
            'cells': 10
        })
        self.assertEqual(response.status_code, 404)

    def test_login_person_maker_forbidden(self):
        self.client.login(
            username='prova1',
            password='cadabra1'
        )

        response = self.client.post(reverse('showcase:manufacture_panel'))
        self.assertRedirects(response, '/members/login/?next=/showcase/manufacturer_panel/')
