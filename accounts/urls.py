from django.urls import path
from django.views.generic import RedirectView


from .views import (
    UserDetailView,
    UserFollowView
    )

app_name = 'profiles'
urlpatterns = [
    # path('', RedirectView.as_view(url='/')),
    # path('', TweetListAPIView.as_view(), name='list'),
    path('<username>/', UserDetailView.as_view(), name='detail'),
    path('<username>/follow/', UserFollowView.as_view(), name='follow'),
    # path('create/', TweetCreateAPIView.as_view(), name='create'),
    # path('<int:pk>/update/', TweetUpdateView.as_view(), name='update'),
    # path('<int:pk>/delete/', TweetDeleteView.as_view(), name='date')
]
