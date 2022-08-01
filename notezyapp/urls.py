
from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name ='index'),
    path('home',views.home,name ='home'),
    path('notes',views.notes,name ='notes'),
    path('signin',views.signin,name = 'signin'),
    path('login',views.login,name='login'),
    path('delete/<int:id>',views.delete,name ='delete'),
    path('logout/',views.logout,name ='logout'),
    
    path('edit/<int:id>',views.edit,name ='edit')
]