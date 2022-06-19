from django.db import models

from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_bio = models.TextField(max_length=150)
    user_contact = models.EmailField(max_length=100)
    user_profile = CloudinaryField('image')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
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
        
    def delete_neigborhood(self):
        self.delete()
    
    def update_neighborhood(self):
        self.save()
        
    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)
    