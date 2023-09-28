from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from ninja import NinjaAPI
from GenrePredict.genre.apps import GenreConfig
import requests

api = NinjaAPI()


@api.get("/getGenre")
def get_genre(request, url: str, **kwargs):
    api_token = GenreConfig.spotify_auth.token
    
    audio_feature = requests.get(url=f"https://api.spotify.com/v1/audio-features/{get_id(url)}",
                                 headers={"Authorization": f"Bearer {api_token}"})
    
    return audio_feature.json()


@api.get("/getImage")
def get_image(request, url: str, **kwargs):
    api_token = GenreConfig.spotify_auth.token

    audio_feature = requests.get(url=f"https://api.spotify.com/v1/tracks/{get_id(url)}",
                                 headers={"Authorization": f"Bearer {api_token}"})

    return audio_feature.json()["album"]["images"][0]["url"]


def get_id(url: str):
    return str(url).split("/")[-1].split("?")[0]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    path('', TemplateView.as_view(template_name='index.html')),
]
