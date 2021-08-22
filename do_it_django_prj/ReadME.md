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

