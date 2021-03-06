from datetime import date

from django.db import IntegrityError
from django.test import TestCase
from .models import Person


class PersonTest(TestCase):

    def test_create_person(self):
        p = Person.objects.create(first_name='Jan', last_name='Twardowski')
        self.assertEqual(p.first_name, 'Jan')
        self.assertEqual(p.last_name, 'Twardowski')

    def test_is_adult(self):
        p1 = Person.objects.create(
            first_name='First',
            last_name='Twardowski',
            date_of_birth=date(2018, 12, 6))
        self.assertFalse(p1.is_adult())

        # p2 = Person.objects.create(
        #     first_name='Second',
        #     last_name='Twardowski',
        #     date_of_birth=date(2000, 12, 5))
        # self.assertTrue(p2.is_adult())
        #
        # p3 = Person.objects.create(
        #     first_name='Third',
        #     last_name='Twardowski',
        #     date_of_birth=date(2000, 12, 6))
        # self.assertTrue(p3.is_adult())
        #
        # p4 = Person.objects.create(
        #     first_name='Fourth',
        #     last_name='Twardowski',
        #     date_of_birth=date(2000, 12, 7))
        # self.assertFalse(p3.is_adult())

    def test_create_invalid_person(self):
        with self.assertRaises(IntegrityError):
            p1 = Person.objects.create(first_name='F1', last_name='L1')
            p2 = Person.objects.create(first_name='F1', last_name='L1')

    def test_connection(self):
        self.client.get('...')
