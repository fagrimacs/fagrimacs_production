from django.test import TestCase
from django.core import mail
from django import forms

from main.forms import ContactForm


class TestMainForms(TestCase):

    def test_invalid_contact_form(self):
        form = ContactForm({
            'name': 'Innocent',
            'message': 'do',
        })

        self.assertFalse(form.is_valid())

    def test_valid_contact_form_sends_email(self):
        form = ContactForm({
            'name': 'Innocent',
            'message': 'At least four words',
        })

        self.assertTrue(form.is_valid())

        form.send_mail()

        self.assertEqual(len(mail.outbox), 1)
