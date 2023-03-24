from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Movie, MovieRating, Tv, TvRating ##
from rango.forms import MovieRatingForm, TvRatingForm
from django.shortcuts import redirect
from django.urls import reverse
from rango.forms import UserForm, UserProfileForm, MovieForm, TvForm ##
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

def HOMEPAGE(request):
    print(request.method)
    print(request.user)
    movie_list = Movie.objects.order_by('title')
    tv_list = Tv.objects.order_by('title')

    context_dict = {}
    context_dict['movies'] = movie_list
    context_dict['shows'] = tv_list

    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    return render(request, 'rango/HOMEPAGE.html', context=context_dict)
    
    
def Search_Shows(request):

    if request.method == "POST":
        searched = request.POST['searched']
        movies = Movie.objects.filter(title__contains=searched)
        shows = Tv.objects.filter(title__contains=searched)
        return render(request, 'rango/Search_Shows.html',{'searched' :searched, 'movies': movies, 'shows': shows})
    else:
        return render(request, 'rango/Search_Shows.html',{})
        

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(request.COOKIES.get('visits', '1'))

    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie
    
    request.session['visits'] = visits

def show_movie(request, movie_name_slug):
    context_dict = {}

    try:
        movie = Movie.objects.get(slug=movie_name_slug)
        ratings = MovieRating.objects.filter(movie=movie)

        context_dict['ratings'] = ratings
        context_dict['movie'] = movie

    except Movie.DoesNotExist:
        context_dict['ratings'] = None
        context_dict['movie'] = None
    
    return render(request, 'rango/movie.html', context=context_dict)

@login_required
def add_movie(request):
    form = MovieForm()

    if request.method == 'POST':
        form = MovieForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/rango/HOMEPAGE/')
        
        else:
            print(form.errors)

    return render(request, 'rango/add_movie.html', {'form': form})

@login_required
def add_ratingmovie(request, movie_name_slug):
    try:
        movie = Movie.objects.get(slug=movie_name_slug)
    except Movie.DoesNotExist:
        movie = None

    username = request.user.username

    if movie is None:
        return redirect('/rango/HOMEPAGE/')

    form = MovieRatingForm()

    if request.method == 'POST':
        form = MovieRatingForm(request.POST)

        if form.is_valid():
            if movie:
                rating = form.save(commit=False)
                rating.movie = movie
                rating.user = username;
                rating.save()
                
                data = form.cleaned_data
                val = getattr(movie, "avgRating")
                if val==-1:
                    movie.avgRating = data['rating']
                else:
                    movie.avgRating = round((val+float(data['rating']))/2, 2)
                movie.save()

                return redirect(reverse('rango:show_movie', kwargs={'movie_name_slug':movie_name_slug}))

        else:
            print(form.errors)

    context_dict = {'form': form, 'movie':movie}
    return render(request, 'rango/add_ratingmovie.html', context=context_dict)

def show_tv(request, tv_name_slug): 
    context_dict = {}

    try:
        tv = Tv.objects.get(slug=tv_name_slug)
        ratings = TvRating.objects.filter(tv=tv)

        context_dict['ratings'] = ratings 
        context_dict['tv'] = tv

    except Tv.DoesNotExist:
        context_dict['ratings'] = None
        context_dict['tv'] = None
    
    return render(request, 'rango/tv.html', context=context_dict)

@login_required
def add_tv(request):
    form = TvForm()

    if request.method == 'POST':
        form = TvForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/rango/HOMEPAGE/')
        
        else:
            print(form.errors)

    return render(request, 'rango/add_tv.html', {'form': form})

@login_required
def add_ratingtv(request, tv_name_slug):
    try:
        tv = Tv.objects.get(slug=tv_name_slug)
    except Tv.DoesNotExist:
        tv = None

    if tv is None:
        return redirect('/rango/HOMEPAGE/')

    username = request.user.username    

    form = TvRatingForm()

    if request.method == 'POST':
        form = TvRatingForm(request.POST)

        if form.is_valid():
            if tv:
                rating = form.save(commit=False)
                rating.tv = tv
                rating.user = username;
                rating.save()
                
                data = form.cleaned_data
                val = getattr(tv, "avgRating")
                if val==-1:
                    tv.avgRating = data['rating']
                else:
                    tv.avgRating = round((val+float(data['rating']))/2, 2)
                tv.save()

                return redirect(reverse('rango:show_tv', kwargs={'tv_name_slug':tv_name_slug}))

        else:
            print(form.errors)

    context_dict = {'form': form, 'tv':tv}
    return render(request, 'rango/add_ratingtv.html', context=context_dict)

def signup(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            register = True

        else:
            print(user_form.errors, profile_form.errors)
    
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'rango/signup.html', context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('rango:HOMEPAGE'))

            else:
                return HttpResponse("Your account is disabled")

        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'rango/login.html')

@login_required
def restricted(request):
    return render(request, 'rango/restricted.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('rango:HOMEPAGE'))