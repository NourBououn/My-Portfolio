from django.db import models
from django.utils import timezone
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True) #we can only have a unique tag for the project 
    
    def __str__(self): #string method when we print out the model
        return self.name
    
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="projects") # like pythons js django kol projet shnua aandu
    link = models.URLField(max_length=200, blank=True) #Link for the github project and blank = true , it's okey to not have a link for the project
    created_at = models.DateTimeField(auto_now_add=True)
    
    #manytomanyfield whenever we create database models we have the ability to relate them together ,  we have project witch is related to some of tags 
    # 3 diff types of relationships , we have one to one : exple one project is associated with only one tag
    # One to manyrelationship : One project is associated with many tags 
    #ManytoMany : many projects associated with many tags 
    
    
    def __str__(self): #string method when we print out the model
        return self.title
    

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="project_images/")
    
    #CASADE means we delete the images if the projects are deleted
    
    def __str__(self): #string method when we print out the model
        return f"{self.project.title} Image"
    
class CV(models.Model):
    file = models.FileField(upload_to='cvs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CV uploaded at {self.uploaded_at}"    