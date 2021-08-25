from django.shortcuts import render
from django.views.generic import ListView
from .models import Post # models 에있는 Post모델 들고옴

class PostList(ListView):
    model = Post
    ordering = "-pk" # 가장 최신값으로 업데이트
# def index(request):
#     # posts = Post.objects.all()  # 모든 Post레코드를 가져와 저장
#     posts = Post.objects.all().order_by('-pk')  # 모든 Post레코드를 가져와 저장 (가장 최신값으로 업데이트)
#
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts' : posts
#         }
#     )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post,
        }
    )