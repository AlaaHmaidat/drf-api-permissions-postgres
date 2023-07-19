from django.test import TestCase

from django.contrib.auth import get_user_model
from .models import Thing
# Create your tests here.

class Thing_test(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username = 'testuser1', password='testpass1')
        testuser1.save()

        testuser2 = Thing.objects.create(name='testname1',owner='testowner1',desc='testdesc1')
        testuser2.save()

    def thing_model(self):
        thing1 = Thing.objects.get(id=1)
        actual_owner = str(thing1.owner)
        actual_name = str(thing1.name)
        actual_desc = str(thing1.desc)

        self.assertEqual(actual_owner,'testowner1')
        self.assertEqual(actual_name,'testname1')
        self.assertEqual(actual_desc,'testdesc1')