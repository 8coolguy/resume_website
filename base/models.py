from django.db import models

# Create your models here.
#should override all of the __str__ functions
class Skill(models.Model):
    skill_str=models.CharField(max_length=50)
    #date=models.DateTimeField('date_asked')
    def __str__(self):
        return self.skill_str
class Project(models.Model):
    url_link=models.URLField(max_length=200)
    descrip_str =models.TextField(max_length=1000)
    title_str=models.CharField(max_length=100)
    date_completed=models.DateField('date_finished')
    image_path=models.ImageField(upload_to='images')
    #skills_used=models.ForeignKey(Skill, on_delete=models.CASCADE)
    def __str__(self):
        return self.title_str

class Experience(models.Model):
    pass
    #weeeeeaaall you know'
    #need to have the skill database object connected here ya know
#class Classe(models.Model):
#    descrip_str=models.TextField(max_length=500)
#    title_str=models.CharField(max_length=100)
class Eduaction(models.Model):
    school_str=models.CharField(max_length=200)
    major_str=models.CharField(max_length=150)
    expec_grad=models.DateField()
    def __str__(self):
        return self.school_str

class Interest(models.Model):
    interest=models.CharField(max_length=100)
    def __str__(self):
        return self.interest
