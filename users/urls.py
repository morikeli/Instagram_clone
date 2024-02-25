from django.urls import path
from . import views
from . import htmx


urlpatterns = [
    path('homepage/', views.HomepageView.as_view(), name='homepage'),
    path('profile/<str:user_id>/', views.SuggestedUserProfileView.as_view(), name='view_user_profile'),
    path('explore/', views.ExplorePostsView.as_view(), name='explore'),
    path('search', views.SearchView.as_view(), name='search'),
    
]

htmx_urlpatterns = [
    path('suggested-user/follow/', htmx.follow_or_unfollow_users_homepage, name='follow_suggested_user'),
    path('<str:user_id>follow/', htmx.follow_or_unfollow_viewed_user, name='follow_viewed_user'),
    path('follow/', htmx.follow_or_unfollow_users_in_profile_page, name='follow_user'),
    path('like/', htmx.like_or_unlike_post, name='like_or_unlike'),
    path('comment/', htmx.add_comment, name='post_comment'),

]

urlpatterns += htmx_urlpatterns
