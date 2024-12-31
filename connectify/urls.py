from django.urls import path
from .import views 
urlpatterns = [
    path('', views.feed_view, name='feed'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/update/', views.update_profile_view, name='update_profile'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('create_post/', views.create_post, name='create_post'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('comment_on_post/<int:post_id>/', views.comment_on_post, name='comment_on_post'),
    path('send_message/', views.send_message, name='send_message'),
]
