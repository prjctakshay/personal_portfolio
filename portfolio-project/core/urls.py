from django.urls import path
from core.views import home_test

urlpatterns = [
    path('', home_test, name='home'),
    # path('', save, name='save'),
    # path('delete/<int:todo_id>/', delete, name= 'delete'),
]