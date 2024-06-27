from django.shortcuts import redirect,render


# Create your views here.
from .models import Post,Category, Comment
from django.core.paginator import Paginator

def blog(request):

    posts = Post.objects.filter(is_published=True).order_by('posted_at')
    categories = Category.objects.all()
    posts = Paginator(posts, 1)
    page = request.GET.get('page')
    posts = posts.get_page(page)

    context = {
        'posts' : posts,
        'categories' : categories,
    }


    return render(request,'blog/blog.html',context)


def post(request, title):
    
    post = Post.objects.get(title = title)
    category = post.category
    related_posts = Post.objects.filter(category = category)

    recent_posts = Post.objects.filter(is_published=True).order_by('posted_at')

    categories = Category.objects.all()
    comments = Comment.objects.filter(post=post)

    context = {
        'related_posts':related_posts,
        'recent_posts': recent_posts,
        'post': post,
        'categories' : categories,
        'comments':comments,
               
    }

    return render (request, 'blog/post.html', context)

def post_comment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        website = request.POST.get('website')
        post_id = request.POST.get('id')
        
        post = Post.objects.get(id = post_id)

        c = Comment(name = name, email = email, website = website, post = post, comment = comment)
        c.save()

        return redirect('post' , title = post.title) 
    return redirect('home')

def search_view(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        

        posts = Post.objects.filter(title__icontains=keyword)
        categories = Category.objects.all()

        context = {
            'posts' : posts,
            'categories' : categories,
        }

    return render(request,'blog/blog.html',context)

def get_category(request,cat):
    
    category = Category.objects.get(name = cat)
    posts = Post.objects.filter(category=category)
    categories = Category.objects.all()

    context = {
        'posts' : posts,
        'categories' : categories,
    }

    return render(request,'blog/blog.html',context)