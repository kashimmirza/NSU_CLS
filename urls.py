from django.urls import include, path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
]