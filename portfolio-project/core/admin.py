from django.contrib import admin
from .models import AboutMe,Skills, SkillMore, MyWork

# Register your models here.

admin.site.register(AboutMe)
admin.site.register(Skills)
admin.site.register(SkillMore)
admin.site.register(MyWork)
