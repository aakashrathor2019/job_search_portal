from django.urls import path,include
from search_job.views import SignUp ,Login ,Home

urlpatterns= [
    path('signup/',SignUp.as_view(),name='signup'),
    path('login/', Login.as_view() , name='login'),
    path('home/', Home.as_view() ,name='home'),
]