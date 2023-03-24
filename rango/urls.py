from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('movie/<slug:movie_name_slug>/', views.show_movie, name='show_movie'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('movie/<slug:movie_name_slug>/add_ratingmovie/', views.add_ratingmovie, name='add_ratingmovie'),
    
    path('tv/<slug:tv_name_slug>/', views.show_tv, name='show_tv'),
    path('add_tv/', views.add_tv, name='add_tv'),
    path('tv/<slug:tv_name_slug>/add_ratingtv/', views.add_ratingtv, name='add_ratingtv'),
    
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),
    path('Search_Shows/', views.Search_Shows, name = 'Search_Shows'),
    path('HOMEPAGE/',views.HOMEPAGE, name='HOMEPAGE'),
]