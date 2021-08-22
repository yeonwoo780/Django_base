from django.contrib import admin
from .models import Post

# 관리자 페이지에 새로운 포스트 작성할수 있는 기능 추가
admin.site.register(Post)

