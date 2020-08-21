from django.test import TestCase
from models import UserProfile

# Create your tests here.
class UserProfileTest(TestCase):
    def setUp(self):
        self.user1 = UserProfile(user='User1',bio="Fake till you make it",image='default.jpg',contact='07456390037')

    def test_instance(self):
        self.assertTrue(isinstance(self.user1,UserProfile))

    
