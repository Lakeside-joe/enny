from django.urls import path
from.views import *
urlpatterns = [
    path('',index,name='index'),
    path('contact',contact,name='contact'),
    path('showcase',showcase,name='showcase'),    
    path('specials',specials,name='specials'),   
    path('all_food',all_food,name='all_food'),  
    path('signout',signout,name='signout'),  
    path('signin',signin,name='signin'),  
    path('signup',signup,name='signup'),  
    path('profile',profile,name='profile'),  
    path('profileupdate',profileupdate,name='profileupdate'),  
    path('passwordupdate',passwordupdate,name='passwordupdate'),  
    path('categories',categories,name='categories'),  
    path('ordermeal',ordermeal,name='ordermeal'),  
    path('shopcart',shopcart,name='shopcart'),  
    path('increase',increase,name='increase'),  
    path('delete',delete,name='delete'),
    path('checkout',checkout,name='checkout'),
    path('category/<str:id>',single_category,name='category'),  
    path('detail/<str:id>',detail,name='detail'),  
]
