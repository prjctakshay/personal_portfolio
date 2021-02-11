from django.urls import path
from core.views import home, test

urlpatterns = [
    path('', home, name='home'),
    path('test', test, name='test'),
    # path('', save, name='save'),
    # path('delete/<int:todo_id>/', delete, name= 'delete'),
]
