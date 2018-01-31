from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    #path('register/', views.register, name='register'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('profile/<str:sap_id>/', views.view_profile, name='view_profile'),
    path('index/', views.index, name='index'),
    #path('index/', views.TemplateView.as_view(template_name='users/index.html'), name='index'),
]