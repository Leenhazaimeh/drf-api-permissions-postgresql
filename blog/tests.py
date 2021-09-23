from django.test import SimpleTestCase

# Create your tests here.

from django.test import SimpleTestCase
from django.contrib.auth import get_user_model
from .models import Blog

# Create your tests here.

class BlogTests(SimpleTestCase):

    @classmethod

    def setUpTest(cls):
        testuser = get_user_model().objects.create_user(username='user', password='0000')
        testuser.save()
        testpost = Blog.objects.create(title='LTUC', body='located at Irbid', author=2)
        testpost.save()
    
    # def test_Blog(self):
    #     post = Blog.objects.get(id=1)
    #     expected_author = f'{post.author}'
    #     expected_title = f'{post.title}'
    #     expected_body = f'{post.body}'
    #     self.assertEqual(expected_author, 'user')
    #     self.assertEqual(expected_title, 'LTUC')
    #     self.assertEqual(expected_body, 'located at Irbid')