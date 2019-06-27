# AlgoReader


requirement.txt
필요한 라이브러리(ipython, django 등)를 설치하여 개발환경 세팅 후 requirements.txt를 만든다.
requirements.txt가 있다면 다음 명령을 통해 동일한 파이썬 패키지들을 한번에 설치할 수 있다.
```shell
$ pip3 freeze > requirements.txt  # 패키지 목록을 txt 파일로 만들기
$ pip3 install -r requirements.txt  # 한번에 패키지 설치
```



