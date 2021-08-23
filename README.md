# 장고 프로젝트 생성

cmd 창에

```
django-admin startproject 프로젝트이름 .
```



프로젝트 잘만들어 졋는지 확인

```
python manage.py runserver
```

http://127.0.0.1:8000/ 로 접속



데이터베이스 생성

```
python manage.py migrate
```

Sqlite3 생김 나중에 대용량 sql 실습예정



데이터베이스 관리자계정 생성

```
(Django_base) PS C:\Anaconda_python\Django_base> python manage.py createsuperuser
Username (leave blank to use 'jung'): jung
Email address: rlckrl0315db@gmail.com
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
(Django_base) PS C:\Anaconda_python\Django_base>
```



서버 실행하여 127.0.0.1:8000/admin/ 으로 접속하여 관리자 계정 확인

-----

-----

-----

-----

----



# Blog 앱과 Page앱 만들기

python manage.py startapp 이름

```
(Django_base) PS C:\Anaconda_python\Django_base> python manage.py startapp blog
(Django_base) PS C:\Anaconda_python\Django_base> python manage.py startapp single_pages
```



blog/models.py에 모델생성 (제목, 내용, 작성일)

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField()

    created_at = models.DateTimeField()
```



데이터 베이스에 Post모델 반영 (아직 setting.py에 blog 앱 등록하지 않아 변경사항 저장 안됨)

```
(Django_base) PS C:\Anaconda_python\Django_base> python manage.py makemigrations
No changes detected
```



settings.py에 blog앱 등록

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'single_pages',
]
```



데이터 베이스에 Post모델 다시반영

```
(Django_base) PS C:\Anaconda_python\Django_base> python manage.py makemigrations
Migrations for 'blog':
  blog\migrations\0001_initial.py
    - Create model Post
```



실제 데이터 베이스에 모델 적용

```
(Django_base) PS C:\Anaconda_python\Django_base> python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying blog.0001_initial... OK
```



## 관리자 페이지에서 첫 포스트 작성하기

blog/admin.py에 Post모델 추가 (관리자 페이지에 새로운 포스트 작성할수 있는 기능 추가)

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```



- 포스트 개선하기

blog/models.py (post로 작성한 제목으로 들고와줌)

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 30) # 제목
    content = models.TextField() # 내용

    created_at = models.DateTimeField() # 작성일

    def __str__(self):
        return f"[{self.pk}]{self.title}"
```



do_it_django_prj/settings.py에 한국 시간으로 변경해줌

```
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False
```



blogs/models.py에 자동으로 작성 시각과 수정 시각 저장

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 30) # 제목
    content = models.TextField() # 내용

    # created_at = models.DateTimeField() # 작성일
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.pk}]{self.title}"
```



모델 수정 후 makemigrations로 장고에게 알린후, migrate로 데이터베이스에 반영. 그리고 서버실행

```
(Django_base) PS C:\Anaconda_python\Django_base> python manage.py makemigrations
Migrations for 'blog':
  blog\migrations\0002_auto_20210822_1859.py
    - Add field update_at to post
    - Alter field created_at on post
(Django_base) PS C:\Anaconda_python\Django_base> python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying blog.0002_auto_20210822_1859... OK
(Django_base) PS C:\Anaconda_python\Django_base> python manage.py runserver
```

-----

-----

-----

----

-----



# URL 설정하기



urls.py 는 표지판 역할

do_it_django_prj/urls.py 



블로그 페이지는 '도메인/blog/포스트의 pk'



자기소개 페이지는 "도메인/about_me/"



- url을 설정해야한다

url 설정하지 않았을시

```
http://127.0.0.1:8000/blog <-- 주소로 들어 갔을시 안나옴

Not Found: /blog
[22/Aug/2021 21:57:26] "GET /blog HTTP/1.1" 404 2099
```



- 방문자가 blog들어왔을시  보이게 설정

do_it_django_prj/urls.py 

```python
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('blog', include('blog.urls')),
    path('admin/', admin.site.urls),
]
```



blog/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    # 이 부분 채울 예정
]
```



## FBV로 페이지 만들기

blog/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index)
]
```



blog/views.py에 index()함수 정의

```python
from django.shortcuts import render

def index(request):
    return render(
        request,
        'blog/index.html',
    )
```



blog/templates/blog/index.html

```html
<!doctype html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Blog</title>
</head>
<body>
    <h1>Blog</h1>
</body>
</html>
```





### 블로그 페이지에 포스트 목록 나열



blog/views.py

```python
from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()  # 모든 Post레코드를 가져와 저장

    return render(
        request,
        'blog/index.html',
        {
            'posts' : posts,
        }
    )
```



blog/templates/blog/index.html

```html
</head>
<body>
    <h1>Blog</h1>

{% for p in posts %}
    <h3>{{p}}</h3>
{% endfor %}
</body>
</html>
```





### Post 모델의 필드값 보여주기



blog/templates/blog/index.html

```html
<body>
    <h1>Blog</h1>

{% for p in posts %}
    <hr/>
    <h2>{{ p.title }}</h2>
    <h4>{{ p.created_at }}</h4>
    <p>{{ p.content }}</p>
{% endfor %}
</body>
</html>
```



blog/views.py

```python
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
```





## FBV로 포스트 상세 페이지 만들기



### 포스트 상세 페이지 URL 정의하기



blog/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('/<int:pk>/', views.single_post_page), #/blog/ 뒤에 int형태의 값이 붙는 형태라면 single 함수로 처리
    path('', views.index),
]
```



blog/views.py에 single_post_page()함수 정의

```
def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post
        }
    )
```



blog/templates/blog/single_post_page.html

```html
<!doctype html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>{{ post.title }} - Blog</title>
</head>

<body>

<nav>
    <a href = "/blog/">Blog</a>
</nav>

<h1>{{ post.title }}</h1>
<h4>{{ post.created_at }}</h4>
<p>{{ post.content }}</p>
<hr/>
<h3>댓글 자리!</h3>

</body>
</html>
```

