from django.shortcuts import render
from django.http import HttpResponse
from .models import AboutMe, Skills, SkillMore, MyWork
# Create your views here.


def home(request):
    # return HttpResponse("<h1>hello</h1>")
    about_me = AboutMe.objects.latest('id')
    skills = Skills.objects.all()
    skills_more = SkillMore.objects.all()
    my_work = MyWork.objects.all()

    data = {
        'about_me': about_me,
        'skills': skills,
        'skills_more': skills_more, 
        'my_work': my_work,
    }
    # print (about_me('user_name'))
    # print(data['about_me'].values('user_name'))
    return render(request, 'core/index.html', {'data': data})
    # obj = AboutMe.objects.order_by('-id')[0]
    user_name = about_me.user_name
    user_profile_pic = about_me.user_profile_pic
    user_profession = about_me.user_profession
    about_me_bio = about_me.about_me_bio
    # return render(request, 'core/index.html', {'user_name': user_name,
    #                                            'user_profile_pic':user_profile_pic,
    #                                           'user_profession': user_profession,
    #                                           'about_me_bio': about_me_bio,
    #                                           'skills':skills,
    #                                           'skills_more':skills_more,
    #                                           'my_work':my_work,
    #                                           })


def test(request):
    # return HttpResponse("<h1>hello</h1>")
    return render(request, 'core/hello.html', {'title': 'sample web page'})
