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
 
 
 
 
 
 
 
 
 
 
 
 
 
 
