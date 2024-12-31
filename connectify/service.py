from .models import Profile, Post,User

def get_user_profile(username):
    try:
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
        posts = Post.objects.filter(user=user).order_by('-created_at')
        return profile, posts
    except (User.DoesNotExist, Profile.DoesNotExist):
        return None, None
