from django.db import models

# Create your models here.

class AboutMe(models.Model):
    user_profile_pic = models.ImageField(upload_to = 'user/profile_pic', null = True, blank = True)
    user_name = models.CharField(max_length=50)
    user_profession = models.CharField(max_length=50)
    about_me_bio = models.CharField(max_length=300)
  
    
class Skills(models.Model):
    skills_text = models.CharField(max_length = 500)
    skill_img = models.ImageField(upload_to = 'user/skills',null=True)

# its represent What I’m good at? in index page
class SkillMore(models.Model):
    skill_name = models.CharField(max_length = 100)
    skill_discription = models.TextField(max_length= 500)
    skill_icon = models.ImageField(upload_to = 'user/what_im_good_icon',null=True)
    
class MyWork(models.Model):
    work_img = models.ImageField(upload_to = 'user/works',null=True)
    work_title = models.CharField(max_length = 100)
    short_discription = models.CharField(max_length = 200)
    git_url = models.URLField(null = True)
    website_url = models.URLField(null = True)
    
    