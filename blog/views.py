from django.shortcuts import render
from .models import Post # models 에있는 Post모델 들고옴

def index(request):
    # posts = Post.objects.all()  # 모든 Post레코드를 가져와 저장
    posts = Post.objects.all().order_by('-pk')  # 모든 Post레코드를 가져와 저장 (가장 최신값으로 업데이트)

    return render(
        request,
        'blog/index.html',
        {
            'posts' : posts
        }
    )
