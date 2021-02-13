  #creation django project and run steps
#check python is installed or not
 python3 --version
 
 <a href="https://www.python.org/downloads">
 if not installed install python first
 </a>
 in linux install >> sudo apt install python3 
 
 create virtual environment inside the directory
 >> python3 -m venv myvenv
 
 activate virtual environment
 >> source myvenv/bin/activate
 
 for install pip or upgrade pip 
 >> python -m pip install --upgrade pip
 
 show installed pip packages
 >> pip list
 
 install django
 >> python -m pip install Django
 
 create requirments.txt file and 
 add installed packages names to that file
 >> pip freeze > requirements.txt
 
 create django-project
 >> django-admin startproject portfolio
 
 best practice name the parent directory
 portfolio to portfolio-project for avoid confusion
 
 to run and test django project
 >> python3 manage.py  runserver
 
 --------------------------------------------------------
 #clone project steps
 existing project run steps
 
 create virtual en
 >> python3 -m venv myvenv
 activate
 >> source myvenv/bin/activate
 
 paste project folder inside the directory
 or clone github project
 
 install django anf required packges inside the 
 requirments.txt
 >>pip install -r requirements.txt
 
 ##if we try without install required packages
 show error like
 >> python3 manage.py runserver

    "" ImportError: Couldn't import Django. Are you sure   it's installed
     and available on your PYTHONPATH environment variable? Did you
     forget to activate a virtual environment? ""

  so first install required packages 
  using the command
  >>pip install -r requirements.txt
  
  go to project dir
  like >> cd project-name
  
  run server
  >> python3 manage.py runserver
  
  run and make your own changes
 
 
 -------------------------------------
 creating app
 DTL(django template language)
 create dir base_template
     inside create base.html
 add template path inside settings.py
 inside TEMPLATES list >dictonary 'DIRS' : '=>>'
      path(os.path.join(BASE_DIR,'base_template')
 #Django tried loading these templates, in this order:top to bottom
 
 in views import >>
  from django.shortcuts import render

  def home_test(request):
    # return HttpResponse("<h1>hello</h1>")
    return render(request, './base.html')
 
  we can also pass some values to that web page 
    return render(request, './base.html', {'title':'sample web page'})
    then add following line to base.html
        <title> {{ title }} </title>


  #base and extend template
  create base.html
  {% block name %}
  
   {% endblock %} 
   
   inside which html we want extend this add>>
   
{% extends 'head.html'%} <!--must 1st tag and syntax same otherwise error-->
 then
 
    {% block name %}
        <h1>hello world {{title}}</h1>
    {% endblock %}
    
------------------
MEDIA_URL = '/media/' 
^is urlil display cheyyunnath aan


MEDIA_ROOT = os.path.join(BASE_DIR,  'media')
^is directory name aan evida aan img save cheyandat aa diectory
in above case images are saved ./media dir
and images are upload in this path and which path 
specified upload_to in models
eg =    skill_img = models.ImageField(upload_to = 'portfolio_images',null=True)
above case img upload to below eg
./media/portfolio_images

in defaul img are saved to portfolio_images enna folderil if it doesnt exist create in base_dir and
img upload to that dir
#above create a dir media the img files are save under the media dir

img upload are work above code but not show if we click in the img dir

so add following code to urls.py
from django.conf.urls.static import static
from django.conf import settings
..........
...........
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

    
   
 
 
 
 
 
 
 
