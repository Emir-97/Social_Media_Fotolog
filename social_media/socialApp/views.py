from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, PostForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def feed(request):
    posts = Posts.objects.all()
    dictionary = {'posts' : posts}
    return render(request, 'socialApp/feed.html', dictionary)

def profile(request, username=None):
    current_user = request.user
    if username and username != current_user:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, 'socialApp/profile.html', {'user':user, 'posts':posts})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'User {username} create')
            return redirect('feed')
    else:
        form = UserRegisterForm()
    dictionary = {'form' : form}
    return render(request, 'socialApp/register.html', dictionary)
@login_required
def post(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = current_user
			post.save()
			messages.success(request, 'Sent Post')
			return redirect('feed')
	else:
		form = PostForm()
	return render(request, 'socialApp/post.html', {'form' : form })

def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship(from_user=current_user, to_user=to_user_id)
    rel.save()
    messages.success(request, f'Follow to {username}')
    return redirect('feed')

def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user.id
    rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
    rel.delete()
    messages.success(request, f'You no longer follow {username}')
    return redirect('feed')
