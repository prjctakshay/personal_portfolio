from django.db import models

# Create your models here.

class AboutMe(models.Model):
    about_me_bio = models.CharField(max_length=300)
  
    
class Skills(models.Model):
    skills_text = models.CharField(max_length = 500)
    # skill_img = models.ImageField()

# its represent What I’m good at? in index page
class SkillMore(models.Model):
    skill_name = models.CharField(max_length = 100)
    skill_discription = models.TextField(max_length= 500)
    # skill_icon = models.ImageField()
    
class MyWork(models.Model):
    # work_img = models.ImageField()
    work_title = models.CharField(max_length = 100)
    short_discription = models.CharField(max_length = 200)
    git_url = models.URLField()
    
    