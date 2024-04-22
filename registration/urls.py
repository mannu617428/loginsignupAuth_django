from django.contrib import admin
from django.urls import path , include
from app1 import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.signupPage , name='Signup'),
    path('login/' , views.loginPage , name = 'Login'),
    path('home/' , views.homePage , name = 'Homepage'),
    path('logout/' , views.logoutPage , name = 'Logout'),
    path('logout/' , auth_views.LoginView.as_view() , name = 'Logout'),
 
    path('social_auth/', include(('social_django.urls', 'social_auth'), namespace='social_auth')),
]





