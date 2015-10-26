"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
Replace this with more appropriate tests for your application.
"""
from django.test import TestCase, RequestFactory
try:
    # Django >= 1.7
    from django.test import override_settings
except ImportError:
    # Django <= 1.6
    from django.test.utils import override_settings

from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse
from django.utils.timezone import utc, localtime
from django.utils import timezone
import json

from notifications import notify
from notifications.models import Notification
from notifications.utils import id2slug


class NotificationTestPages(TestCase):

    def setUp(self):
        self.message_count = 10
        self.from_user = User.objects.create_user(username="from", password="pwd", email="example@example.com")
        self.to_user = User.objects.create_user(username="to", password="pwd", email="example@example.com")
        self.to_user.is_staff = True
        self.to_user.save()
        for i in range(self.message_count):
            notify.send(self.from_user, recipient=self.to_user, verb='commented', action_object=self.from_user)


    def test_all_messages_page(self):
        response = self.client.get('/inbox/notifications/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.context['notifications']),len(self.to_user.notifications.all()))

    def test_unread_messages_pages(self):
        response = self.client.get('/inbox/notifications/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.context['notifications']),len(self.to_user.notifications.unread()))
        self.assertEqual(len(response.context['notifications']), self.message_count)

        for i,n in enumerate(self.to_user.notifications.all()):
            if i%3 == 0:
                response = self.client.get(reverse('notifications:mark_as_read',args=[id2slug(n.id)]))
                self.assertEqual(response.status_code,302)

        response = self.client.get(reverse('notifications:mark_all_as_read'))
        self.assertRedirects(response,reverse('notifications:all'))
        response = self.client.get(reverse('notifications:unread'))
        self.assertEqual(len(response.context['notifications']),len(self.to_user.notifications.unread()))
        self.assertEqual(len(response.context['notifications']),0)

   