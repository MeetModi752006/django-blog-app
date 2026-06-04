from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .models import Post
from .forms import PostForm


def home(request):
    """Public homepage showing all published posts."""
    posts = Post.objects.filter(published=True)
    return render(request, 'blog/home.html', {'posts': posts})


def post_detail(request, pk):
    """Show a single post. Unpublished posts visible only to author or admin-role users."""
    post = get_object_or_404(Post, pk=pk)

    # Restrict unpublished posts
    if not post.published:
        if not request.user.is_authenticated:
            raise PermissionDenied
        if request.user != post.author and not request.user.profile.is_admin_role():
            raise PermissionDenied

    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_create(request):
    """Allow any logged-in user to create a new post."""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # assign the logged-in user as author
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form': form, 'title': 'New Post'})


@login_required
def post_edit(request, pk):
    """Allow the author (or admin-role user) to edit a post."""
    post = get_object_or_404(Post, pk=pk)

    # Permission check: only author or admin-role can edit
    if request.user != post.author and not request.user.profile.is_admin_role():
        raise PermissionDenied

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {'form': form, 'title': 'Edit Post'})


@login_required
def my_posts(request):
    """Show all posts (published + drafts) belonging to the logged-in user."""
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'blog/my_posts.html', {'posts': posts})


@login_required
def post_delete(request, pk):
    """Allow the author (or admin-role user) to delete a post."""
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.author and not request.user.profile.is_admin_role():
        raise PermissionDenied

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted.')
        return redirect('blog:home')

    return render(request, 'blog/post_confirm_delete.html', {'post': post})
