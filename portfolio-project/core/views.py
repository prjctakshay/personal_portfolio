from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def home_test(request):
    # return HttpResponse("<h1>hello</h1>")
    return render(request, 'core/index.html', {'title':'sample web page'})
def test(request):
    # return HttpResponse("<h1>hello</h1>")
    return render(request, 'core/hello.html', {'title':'sample web page'})
