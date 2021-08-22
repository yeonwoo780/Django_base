# 부트스트랩 알아보기

## 부트스트랩 CSS 자바스크립트 적용

1. getbootstrap.com에 접속후 부트스트랩 4.5버젼 다운

   

2. 압축푼 후 bootstrap.min.css, bootstrap.min.css.map 파일만 들고옴



3. index.html, about_me.html에 head부분에 css 적용

```html
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>about me</title>
    <link href="./bootstrap4/css/bootstrap.min.css" rel="stylesheet" type="text/css">

    <script type="text/javascript" src="what_time_is_it.js"></script>
</head>
```



4. js 코드 적용 index.html, about_me.html의 body 끝부분에 js 적용

   https://getbootstrap.com/docs/4.5/getting-started/download/

   위의 jsDelivr이용

```html
<body>
	(...생략...)
    <a href = "index.html">첫 화면으로 가기</a>
    <img src="images/boys_and_father.jpg" height="400px">

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js" integrity="sha384-w1Q4orYjBQndcko6MimVbzY0tgp4pWB4lZ7lr30WKz0vr/aWKhXdBNmNb5D92v7s" crossorigin="anonymous"></script>
</body>
```



5. Components의 내비게이션 바 적용

```html
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">Navbar</a>
      	(...생략...)
        </div>
    </nav>
```



6. 부트스트랩 css에 정의해놓은 container 사용

about_me.html 확인

```html
    <div class="container">
        <h1>About Me</h1>
        <h2>정연우 입니다. </h2>

        <p>Django로 웹사이트 만들기</p>

        <button onclick="whatTimeIsIt()">현재시간</button>
        <hr/>
        
        <a href = "index.html">첫 화면으로 가기</a>
        <img src="images/boys_and_father.jpg" height="400px">
	 </div>
    (...생략...)
```

양쪽에 여백이 생김



navbar에도 적용해봄



7. grid로 웹페이지 비율 나누기(12 기준)

비율 9대 3만듦

```html
    <div class="container">
        <div class = "row">
            <div class = "col-9">
                <h1>About Me</h1>
                <h2>정연우 입니다. </h2>

                <p>Django로 웹사이트 만들기</p>

                <button onclick="whatTimeIsIt()">현재시간</button>
                <hr/>
                
                <a href = "index.html">첫 화면으로 가기</a>
            </div>

            <div class = "col-3">
                <img src="images/boys_and_father.jpg" class="img-fluid w-100">
                <!-- 높이가 3칸짜리 열에 해당하는 부분의 폭에 꽉차게 적용 -->
            </div>
        </div>
    </div>
```



- 화면 크기에 따라 구성도 변경

Documentation > Layout > Grid

```html
    <div class="container">
        <div class = "row">
			(...생략...)
        </div>

        <div class="container">
            <div class="row">
                <div class="col-sm bg-info">
                    One of three columns
                </div>
                <div class="col-sm bg-secondary">
                    One of three columns
                </div>
                <div class="col-sm bg-warning">
                    One of three columns
                </div>
            </div>
        </div>
        
    </div>

```

위의 배경색은 Documetation > Utilities > Colors 이용



8. spacing으로 간격주기

마진, 패딩 이용



- 내비게이션 바에 마진 넣기

  mt-숫자는 위에만 마진(margin top), mb-숫자는 아래에만 마진(margin bottom), my-숫자는 위아래

```html
    <div class="container">
        <div class = "row my-3">
            <div class = "col-9">
                <h1>About Me</h1>
                <h2>정연우 입니다. </h2>

                <p>Django로 웹사이트 만들기</p>

                <button onclick="whatTimeIsIt()">현재시간</button>
                <hr/>
                
                <a href = "index.html">첫 화면으로 가기</a>
            </div>
			(...생략...)

    </div>
```



- 내비게이션 바 오른쪽 정렬

  ml-auto 는 왼쪽 마진 확보, mr-auto 는 오른쪽 마진 확보

  ```html
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
  			(...생략...)
              </ul>
  
              <ul class="navbar-nav ml-auto">
                  <li class="nav-item">
                      <a class="nav-link" href="#">Log In</a>
                  </li>
              </ul>
              </div>
          </div>
      </nav>
  ```

  위랑 결과 같음

  ```html
              <ul class="navbar-nav  mr-auto">
                  <li class="nav-item active">
                  <a class="nav-link" href="./index.html">Home <span class="sr-only">(current)</span></a>
                  </li>
                  <li class="nav-item">
                  <a class="nav-link" href="./blog_list.html">Blog</a>
                  </li>
                  <li class="nav-item">
                  <a class="nav-link" href="./about_me.html">About me</a>
                  </li>
                  <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                      Dropdown link
                  </a>
                  <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                      <a class="dropdown-item" href="#">Action</a>
                      <a class="dropdown-item" href="#">Another action</a>
                      <a class="dropdown-item" href="#">Something else here</a>
                  </div>
                  </li>
              </ul>
  
  			(...밑의값 변경시 똑같이 나옴...)
  			<!--<ul class="navbar-nav ml-auto">-->
  			<ul class="navbar-nav">
  ```





## 부트스트랩으로 웹사이트 모양 만들기

- 부트스트랩 적용

start bootstrap의 Blog Home 의 index.html 참조

ctrl + U눌러서 원하는 코드 참조 복사





- Pagination 이동버튼 추가

```html
                <!-- Blog post-->
				(...생략...)

                <!-- Pagination-->
                <nav aria-label="Pagination">
                    <hr class="my-0" />
                    <ul class="pagination justify-content-center my-4">
                        <li class="page-item disabled"><a class="page-link" href="#" tabindex="-1" aria-disabled="true">Newer</a></li>
                        <li class="page-item active" aria-current="page"><a class="page-link" href="#!">1</a></li>
                        <li class="page-item"><a class="page-link" href="#!">2</a></li>
                        <li class="page-item"><a class="page-link" href="#!">3</a></li>
                        <li class="page-item disabled"><a class="page-link" href="#!">...</a></li>
                        <li class="page-item"><a class="page-link" href="#!">15</a></li>
                        <li class="page-item"><a class="page-link" href="#!">Older</a></li>
                    </ul>
                </nav>
                
            </div>

            <div class="col-md-4 col-lg-3">

                 <!-- Search widget-->
                (...생략...)
```

