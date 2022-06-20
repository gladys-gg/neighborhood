from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.


# Neighbourhood Model Tests
class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        # create an admin user
        self.admin = User.objects.create_superuser(
            username='gladys',
            password='gladys'
        )
        self.neighbourhood = NeighbourHood(
            name='Test Neighbourhood', location=self.location, occupants_count=10, admin_id=self.admin.id)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood, NeighbourHood))

    def test_save_method(self):
        self.neighbourhood.create_neigborhood()
        neighbourhoods = NeighbourHood.objects.all()
        self.assertTrue(len(neighbourhoods) > 0)

    def test_delete_method(self):
        self.neighbourhood.create_neigborhood()
        self.neighbourhood.delete()
        neighbourhoods = NeighbourHood.objects.all()
        self.assertTrue(len(neighbourhoods) == 0)
        
        
class BusinessTestCase(TestCase):
    '''
    setup
    '''
    def setUp(self):
        self.business = Business(name='boutique',image='cloudinary image',user='1',NeighborHood='1')
    '''
    test instance of business
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))
        '''
        test for save instance of business
        '''
    def test_save_business(self):
        self.business.save_business()
        name = Business.objects.all()
        self.assertTrue(len(name)>0)