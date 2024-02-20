from django.urls import path
from . import views
from django.contrib import admin
# from .views import index,traffic_check_index,traffic_check,speed_check_index,trackMultipleObjects,challan
from .views import UserLoginAPIView, UserLogoutAPIView
urlpatterns = [
    # path('login/', views.user_login, name='login'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('signup/', views.user_signup, name='signup'),
    # path('logout/', views.user_logout, name='logout'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout'),
    path('admin/', admin.site.urls, name='admin'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
]
