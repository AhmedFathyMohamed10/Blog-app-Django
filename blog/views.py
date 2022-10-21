from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comment
from django.db.models import Q
from django.utils import timezone


def index(request):
    
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    
    return render(request, "pages/index.html", context)

def about(request):
    return render(request, "pages/about.html")


def post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, "pages/post.html", context)



def search(request):

    if request.method == 'POST':
        
        search = request.POST['query']
        posts = Post.objects.filter(Q(title__icontains=search) | Q(content__icontains=search))

        context = {
            'posts': posts
        }

        return render(request, "pages/search.html", context)

    return render(request, "pages/search.html")


def create(request):

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['body']
        # get logged in user
        author = request.user
        time_posted = timezone.now()
        # add two hours to the time
        time_posted = time_posted + timezone.timedelta(hours=2) # this is for testing purposes

        post = Post(title=title, content=content, author=author, date_posted=time_posted)
        post.save()
        
        return redirect('index')
        

    return render(request, "pages/create.html")


def comment_on_post(request, post_id):

    if request.method == 'POST':
        comment = request.POST['comment']
        author = request.user
        time_posted = timezone.now()
        # add two hours to the time
        time_posted = time_posted + timezone.timedelta(hours=2) # this is for testing purposes

        post = Post.objects.get(id=post_id) # get the post

        # create a comment
        comment = Comment(comment=comment, author=author, date_posted=time_posted, post_id=post)
        comment.save()

        return render(request, "pages/post.html", {'post': post})

    return render(request, "pages/post.html")

