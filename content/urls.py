from django.urls import path
from .views import UploadFeed, mainprofile, Main, UploadReply, ToggleLike, ToggleBookmark

app_name= 'content'
urlpatterns = [
    path('upload', UploadFeed.as_view()),
    path('reply', UploadReply.as_view()),
    path('like', ToggleLike.as_view()),
    path('bookmark',ToggleBookmark.as_view()),
    path('mainprofile', mainprofile.as_view()),
    path('main',Main.as_view()),
]