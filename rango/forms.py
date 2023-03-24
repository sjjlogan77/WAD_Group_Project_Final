from django import forms
from rango.models import MovieRating, Movie, TvRating, Tv, UserProfile
from django.contrib.auth.models import User

class MovieForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the movie name.")
    releaseDate = forms.CharField(max_length=128, help_text="Please enter the movie release date.")
    # slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Movie
        fields = ('title', 'releaseDate',)

class MovieRatingForm(forms.ModelForm):
    rating = forms.CharField(max_length=2, help_text="Please enter your rating for the movie out of 10")

    class Meta:
        model = MovieRating
        exclude = ('movie', 'user',)


class TvForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the tv show's name.")
    releaseDate = forms.CharField(max_length=128, help_text="Please enter the tv show's release date.")
    # slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Tv
        fields = ('title', 'releaseDate',)

class TvRatingForm(forms.ModelForm):
    rating = forms.CharField(max_length=2, help_text="Please enter your rating for the Tv show out of 10")

    class Meta:
        model = TvRating
        exclude = ('tv', 'user',)




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('age', 'picture')
