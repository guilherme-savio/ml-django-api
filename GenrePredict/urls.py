from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from GenrePredict.genre.apps import GenreConfig
import requests

api = NinjaAPI()

@api.get("/getGenre")
def get_genre(request, url: str, **kwargs):
    music_id = str(url).split("/")[-1].split("?")[0]
    api_token = GenreConfig.spotify_auth.token
    
    audio_feature = requests.get(url=f"https://api.spotify.com/v1/audio-features/{music_id}", 
                                 headers={"Authorization":f"Bearer {api_token}"})
    
    return audio_feature.json()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]
