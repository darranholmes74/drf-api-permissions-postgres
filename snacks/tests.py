from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Snacks


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_post = Snacks.objects.create(
            owner = testuser1,
            name = 'Green Eggs and Ham',
            description = 'I do not like green eggs and ham, Sam I  am.'
        )
        test_post.save()

    def test_blog_content(self):
        snacks = Snacks.objects.get(id=1)
        actual_owner = str(snacks.owner)
        actual_name = str(snacks.name)
        actual_description = str(snacks.description)
        self.assertEqual(actual_owner, 'testuser1')
        self.assertEqual(actual_name, 'Green Eggs and Ham')
        self.assertEqual(actual_description, 'I do not like green eggs and ham, Sam I  am.')

