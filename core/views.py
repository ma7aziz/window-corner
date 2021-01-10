from django.shortcuts import render
from .models import Post, Product

# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('-timestamp')[:3]
    products = Product.objects.all()
    return render(request, 'core/index.html', {'posts': posts, 'products': products})


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')


def news(request):
    posts = Post.objects.all().order_by('-timestamp')
    return render(request, 'core/news.html', {'posts': posts})


def post(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'core/post.html', {'post': post})


def products(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})


def single_product(request, name):
    product = Product.objects.get(name=name)

    return render(request, 'products/single.html', {'product': product})
