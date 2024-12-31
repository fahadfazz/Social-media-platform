from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, Like, Comment, Follow, Notification, Message
from .forms import SignupForm, PostForm, CommentForm, MessageForm, ProfileForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.http import Http404
from .service import get_user_profile
from .models import Profile
from .forms import ProfileUpdateForm
# Create your views here.
# Feed View

from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required



@login_required
def feed_view(request):
    posts = Post.objects.all()
    for post in posts:
        post.has_liked = post.likes.filter(user=request.user).exists()  # Use 'likes' if you defined related_name='likes'
        post.like_count = post.likes.count()  # Correct way to get the like count
    return render(request, 'feed.html', {'posts': posts})

import logging

logger = logging.getLogger(__name__)

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a new profile for the user
            profile = Profile.objects.filter(user=user).first()
            user = authenticate(username=user.username, password=form.cleaned_data.get('password1'))
            login(request, user)
            return redirect('feed')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# Login View
def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            error = "Invalid username or password."
    return render(request, 'user_login.html', {'error': error})


# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# Profile View
@login_required

def profile_view(request, username):
    user = get_object_or_404(User, username=username)  # Get user by username
    profile = user.profile  # Assuming you have a Profile model linked to the User model
    # Get all posts by the user
    posts = Post.objects.filter(user=profile.user).order_by('-created_at')

    return render(request, 'profile.html', {'profile': profile, 'posts': posts})

@login_required
def update_profile_view(request):
    profile = request.user.profile  # Get the logged-in user's profile

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()  # Save the updated profile
            return redirect('profile', username=request.user.username)  # Redirect to the profile page after saving
    else:
        form = ProfileUpdateForm(instance=profile)  # Pre-populate the form with the current profile data

    return render(request, 'update_profile.html', {'form': form})


# Post Creation
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})

# Like Post
@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()  # Unlikes if already liked
    return redirect('feed')

# Comment on Post
@login_required
def comment_on_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('feed')
    else:
        form = CommentForm()
    return render(request, 'comment_create.html', {'post': post, 'form': form})


# Send Message
@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = MessageForm()
    return render(request, 'send_message.html', {'form': form})


# Create your views here.
