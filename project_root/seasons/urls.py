from django.urls import path
from . import views
from .views import mainvote_counts

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('check_auth/', views.check_auth, name='check_auth'),
    path('<str:season_name>/', views.season_view, name='season_view'),
    path('api/mainvote_counts/', mainvote_counts, name='mainvote_counts'),
]