from django.db import models

# Create your models here.
class Skills(models.Model):
    skill_str=models.CharField(max_length=50)
    date=models.DateTimeField('date_asked')

    def __str__(self):
        return self.skill_str
class Projects(models.Model):
    url_link=models.URLField(max_length=200)
    descrip_str =models.TextField(max_length=1000)
    title_str=models.CharField(max_length=100)
    date_completed=models.DateTimeField('date_finished')
    image_path=models.CharField(max_length=100)
    skills_used=models.ForeignKey(Skills, on_delete=models.CASCADE)
    def __str__(self):
        return self.title_str

class Jobs(models.Model):
    pass
    #weeeeeaaall you know'
    #need to have the skill database object connected here ya know
class Eduaction(models.Model):
    gpa_flt =models.
    school_str=models.CharField(max_length=200)
    major_str=models.CharField(max_length=150)
    expec_grad=models.IntegerField()
    cool_classes=models.ForeignKey(Class), on_delete)
class Interests(models.Model):
    image_path=models.CharField(max_length=100)
    interest=models.CharField(max_length)
    date=models.DateTimeField('date_asked')
