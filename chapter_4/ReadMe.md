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