from django.urls import path

import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../tweets'))
from tweets.api.views import TweetListAPIView

app_name = 'profiles-api'
urlpatterns = [
    path('<username>/tweet/', TweetListAPIView.as_view(), name='list'),  # /api/tweet/create/
]
