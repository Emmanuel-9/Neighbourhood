from django.test import TestCase
from models import Business,Neighbourhood

# Create your tests here.
class BusinessTest(TestCase):
    def setUp(self):
        self.real_estate = Business(name='Agribusiness',user='Martin',neighbourhood='Eastlands',email='martin@info.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.real_estate,Business))


class NeighbourhoodTest(TestCase):
    def setUp(self):
        self.juja = Neighbourhood(name='Juja',location='Kiambu',occ_count=4)

    def test_instance(self):
        self.assertTrue(isinstance(self.juja,Neighbourhood))        