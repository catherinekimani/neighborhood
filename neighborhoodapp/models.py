from django.db import models

from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField

# Create your models here.
class Neighborhood(models.Model):
    admin = models.ForeignKey(User,on_delete=models.CASCADE)
    hood_name = models.CharField(max_length=100)
    hood_location = models.CharField(max_length=100)
    hood_descr = models.CharField(max_length=100)
    hood_image = CloudinaryField('hood')
    occupants_count = models.IntegerField(null=True, blank=True)
    hospital_tel = models.IntegerField(null=True, blank=True)
    police_count = models.IntegerField(null=True,blank=True )
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.hood_name}'
    
    def create_neigborhood(self):
        self.save()
        
    @classmethod
    def search_hood(cls, hood_name):
        return cls.objects.filter(hood_name__icontains=hood_name).all()
    
    def delete_neigborhood(self):
        self.delete()
    
    def update_neighborhood(self):
        self.save()
        
    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)
    
    @classmethod
    def search_hood(cls, hood_name):
        return cls.objects.filter(hood_name__icontains=hood_name).all()
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_bio = models.TextField(max_length=150)
    user_contact = models.EmailField(max_length=100)
    user_profile = CloudinaryField('image')
    location = models.CharField(max_length=100,blank=True,null=True)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,blank=True,null=True)
    
    def __str__(self):
        return f'{self.user} Profile'
    
    
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image')
    created_on = models.DateTimeField(auto_now_add=True)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,blank=True,null=True)
    
    
    def save_post(self):
        self.save()
        
    def delete_post(self):
        self.delete()
        
    def __str__(self):
        return f'{self.title}'
    
    
class Business(models.Model):
    business_name = models.CharField(max_length=100)
    business_email = models.EmailField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.business_name}'
    
    def create_business(self):
        self.save()

    def update_business(self):
        self.save()
        
    def find_business(cls, business_id):
        return cls.objects.filter(id=business_id)
        
    @classmethod
    def search_results(cls, business_name):
        return cls.objects.filter(business_name__icontains=business_name).all()
        
    def delete_business(self):
        self.delete()