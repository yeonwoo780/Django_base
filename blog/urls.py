from django.urls import path
from . import views

urlpatterns = [
    # path('<int:pk>/', views.single_post_page), #/blog/ 뒤에 int형태의 값이 붙는 형태라면 single 함수로 처리
    path('<int:pk>/', views.PostDetail.as_view()),

    # path('', views.index),
    path('', views.PostList.as_view()),
]