# from django.shortcuts import render


# def index(request):
# return render(request, "videoapp/index.html")

from django.shortcuts import render
from TikTokApi import TikTokApi


def index(request):
    videos = []
    with TikTokApi() as api:
        videos = api.trending.videos(count=10)
        print(videos)
    # Render the template with the videos.
    return render(request, "videoapp/index.html", {"videos": videos})
