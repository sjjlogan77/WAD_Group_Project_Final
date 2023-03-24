from django.contrib import admin
from rango.models import Movie, MovieRating, Tv, TvRating, UserProfile

class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

class MovieRatingAdmin(admin.ModelAdmin):
    list_display = ('rating', 'movie')

class TvAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

class TvRatingAdmin(admin.ModelAdmin):
    list_display = ('rating', 'tv')


admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieRating, MovieRatingAdmin)
admin.site.register(Tv, TvAdmin)
admin.site.register(TvRating, TvRatingAdmin)
admin.site.register(UserProfile)

