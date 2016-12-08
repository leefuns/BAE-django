from django.shortcuts import render
from blog.models import MetaInfo, Article

# Create your views here.
def index(request):
    metainfo = MetaInfo.objects.all()
    for info in metainfo:
        keywords = info.web_keywords
        description= info.web_description
    articles = Article.objects.order_by("-id")
    return render(request,'index.html',locals())

def python(request):
    return render(request,'python.html',locals())

def notes(request):
    return render(request,'notes.html',locals())

def memo(request):
    return render(request,'memo.html',locals())

def share(request):
    return render(request,'share.html',locals())

def about(request):
    return render(request,'about.html',locals())

def post(request,pk):
    posts = Article.objects.order_by("id")[int(pk)-1]
    title = posts.title
    img = posts.img
    time = posts.publish_time
    author = posts.author
    content = posts.content
    return render(request,'post.html',locals())