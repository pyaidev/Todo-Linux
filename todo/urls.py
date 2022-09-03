from django.urls import path
from .views import home, create, update, delete

urlpatterns = [
    path('', home),
    path('create/', create),
    path('update/<int:pk>/', update),
    path('delete/<int:pk>/', delete),

]