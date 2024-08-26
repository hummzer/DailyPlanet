from django.shortcuts import render

# We'll need 3 view functions: Index, Detail and Category

from django.http import HttpResponseRedirect
from main.forms import CommentForm
from django.shortcuts import render
from main.models import Post, Comment

#This will display a list of all your posts.
def index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
            "posts": posts,
    }

    return render(request, "main/index.html", context)

#This will display posts of a specific category
def category(request, category):
    posts = Post.objects.filter(
            categories__name__contains=category
            ).order_by("-created_on")
    context = {
            "category": category,
            "posts": posts,
    }

    return render(request, "main/category.html", context)

#This will display a full post, its comments and form to create new comments
def detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }

    return render(request, "main/detail.html", context)
