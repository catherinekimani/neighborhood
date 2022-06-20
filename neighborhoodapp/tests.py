from django.test import TestCase
from .models import *
# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.user = User(username='moringa',email="moringa@gmail.com", password='kate')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()
        
class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='moringa',email="moringa@gmail.com")
        self.post = Post.objects.create(title='titletest', image='img.png', description='post test', user=self.user)
    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))
        
    def test_save_post(self):
        self.post.save()
        
    def test_delete_post(self):
        self.post.save()

class BusinessTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='moringa',email="moringa@gmail.com")
        self.business =Business.objects.create(business_name='businesstest', business_email='kay@gmail.com', user=self.user)
    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))
        
    def test_save_post(self):
        self.business.save()
        
    def test_delete_post(self):
        self.business.save()

class HoodTest(TestCase):
    def setUp(self):
        self.admin = User.objects.create(username='moringa',email="moringa@gmail.com")
        self.hood =Neighborhood.objects.create(hood_name='hoodtest', hood_location='nairobi',hood_descr='descr',hood_image ='img.png',occupants_count=5,hospital_tel=15555,police_count=999, admin=self.admin)
    def test_instance(self):
        self.assertTrue(isinstance(self.hood, Neighborhood))
        
    def test_save_post(self):
        self.hood.save()
        
    def test_delete_post(self):
        self.hood.save()
    
