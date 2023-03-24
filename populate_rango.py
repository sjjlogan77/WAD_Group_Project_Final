import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WAD_group_project.settings')

import django
django.setup()
from rango.models import Movie, MovieRating, Tv, TvRating

def populate():
    
    harry_potter_ratings = {"Jeff":5, "GoldiLocks":6, "pear":8, "Ian":9, "Amelia Pond":3} 
    cars_ratings = {"Kyle":10, "Wax Motson":7, "Jeff":7, "JasmineThePlant":9, "Kahn, Gengis":8}
    home_alone_ratings = {"Kyle":5, "Wax Motson":7, "pear":6, "Kahn, Gengis":9, "Amelia Pond":3}
    
    hp_data = {'ratings':harry_potter_ratings, 'date': '1982-01-20'}
    cars_data = {'ratings':cars_ratings, 'date': '1992-02-22'}
    home_lonely_data = {'ratings':home_alone_ratings, 'date': '2001-12-24'}
    
    movies = {'Harry Potter and the Philosiphers Stone': hp_data, 
              'Cars': cars_data, 
              'Home Alone': home_lonely_data}
    
    doctor_who_ratings = {"Jeff":10, "GoldiLocks":9, "apple":8, "Ian":9, "Amelia Pond":10} 
    boss_baby_back_in_business_ratings = {"Kyle":6, "Wax Motson":4, "Jeff":7, "JasmineThePlant":9, "Kahn, Gengis":7} 
    stranger_things_ratings = {"Kyle":10, "Wax Motson":8, "pear":8, "Kahn, Gengis":8, "Amelia Pond":8} 
    
    doctor_who_data = {'ratings':doctor_who_ratings, 'date': '1963-11-23'}
    stranger_things_data = {'ratings':stranger_things_ratings, 'date': '2015-05-17'}
    boss_baby_data = {'ratings':boss_baby_back_in_business_ratings, 'date': '2009-03-19'}
    
    shows = {'Doctor Who': doctor_who_data,
             'Stranger Things': stranger_things_data, 
             'Boss Baby: Back in Business': boss_baby_data}
    
    for movie, movie_data in movies.items():
        d = movie_data['date']
        m = add_movie(movie, d)
        
        total=0
        for user, rating in movie_data['ratings'].items():
            add_movie_rating(m, rating, user)
            total+=rating
        add_movie(movie, d, total/5)
        
    for show, tv_data in shows.items():
        d = tv_data['date']
        s = add_show(show, d)
        
        total=0
        for user, rating in tv_data['ratings'].items():
            add_tv_rating(s, rating, user)     
            total+=rating            
        add_show(show, d, total/5)
        
    for m in Movie.objects.all():
        for r in MovieRating.objects.filter(movie=m):
            print(f'- {m}: {r.user} - {r}')
            
    for s in Tv.objects.all():
        for r in TvRating.objects.filter(tv=s):
            print(f'- {s}: {r.user} - {r}')
            
def add_movie_rating(movie, rating, user):
    r = MovieRating.objects.get_or_create(movie=movie, rating=rating, user=user)[0]
    r.save()
    return r
    
def add_movie(title, releaseDate, avg=-1):
    m = Movie.objects.get_or_create(title=title, releaseDate=releaseDate)[0]
    m.avgRating = avg
    m.save()
    return m
    
def add_tv_rating(show, rating, user):
    r = TvRating.objects.get_or_create(tv=show, rating=rating, user=user)[0]
    r.save()
    return r
    
def add_show(title, releaseDate, avg=-1):
    s = Tv.objects.get_or_create(title=title, releaseDate=releaseDate)[0]
    s.avgRating = avg
    s.save()
    return s
    
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()