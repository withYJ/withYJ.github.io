# GIT 의 필요성 및 사용법

### Intro - GIT을 왜 쓰나?

1. 파일의 변경 내역을 내 컴퓨터 또는 원격 저장소에 저장하여 버전관리해준다.
2. branch, merge 가 쉽다.
3. 속도와 성능이 좋다
4. 분산 작업에 좋다
5. 데이터의 보장성
6. 준비단계(Staging area)가 있다.
7. 오픈소스라 무료다!!

위 내용은 아래 링크에서 골자만 가져온 것이므로 자세한 내용은 아래 링크 참고하길 바람

http://flowerykeyboard.tistory.com/9  

<br>

GIT 개념은 아래 링크를 보며 추가적으로 이해해 나가면 좋을 것 같다.

https://rhostem.github.io/posts/2017-01-07-git-basic/  

<br>

GitHub 은 Local에서 작업한 Git의 내용을 원격으로 저장할 저장소 역할을 하는 공간이다.  

<br>

***

### 1. GIT 설치 & 업데이트 - Windows 기준

1) 아래 링크에서 자신의 OS 환경에 맞게 다운로드 한다.

https://git-scm.com/downloads  

<br>

2) 설치 옵션은 Windows 의 경우 아래 참고하면 된다.

http://igotit.tistory.com/entry/Git-%EC%9C%88%EB%8F%84%EC%9A%B0%EC%9A%A9-%EC%84%A4%EC%B9%98  

<br>

3) 이미 설치되어 있고 업데이트가 필요하다면 cmd 창에서(Windows 키 + r 눌러서 cmd 입력하면  cmd 창 열림) 아래와 같이 입력한다.  

>  c: ~ ~ >git --version						# git version 확인

> c: ~ ~ >git update-git-for-windows			# git 최신 버젼 다운로드 및 설치 진행

말이 업데이트지 새버전 설치하는 것이랑 같기 때문에 설치 옵션 재설정 해줘야 하고, 이는 2) 를 참고하면 된다.  

참고) mac 의 경우 update 진행 방법 https://medium.com/@katopz/how-to-upgrade-git-ff00ea12be18  

<br>

***

### 2. Git 사용 및 GitHub에 파일 올려보기

##### 1) user.name , user.email 초기 설정하기

cmd 창에 아래와 같이 입력해 보자.

> c: ~~ >git config --global user.name		# 현재 로컬 컴퓨터에 설정된 git user.name 조회

> c: ~~ >git config --global user.email		# 현재 로컬 컴퓨터에 연동된 github email 조회  

<br>

처음 설치하면 아무것도 설정되어 있지 않을 것이다. 이제 설정해보자.

> c: ~~ >git config --gobal user.name "여기에 이름을 설정해 주세요"

> c: ~~ >git config --global user.email "여기에 GitHub가입에 사용한 이메일 주소를 적어주세요"  

<br>

##### 2) 온라인 저장소 만들기 (이미 GitHub에서 repository 만드신 분은 점프하세요!)

![Alt text](/images/git1_1.png)

<br>

눌리고 들어가면 우측 상단에 **NEW** 를 눌러주고 repository를 만든다. (아래는 예시)

![Alt text](/images/git1_2.png)

Repository name은 프로젝트 명이나 각자의 목적에 맞게 적어주면 된다. 최상위 폴더명이라 생각하면 쉽게 이해될 것 같다.

Description은 Repository 내용에 대한 간단한 소개글이라 생각하면 된다. (선택사항임)

Public 으로 설정하, Private 사용하고 싶으면 유료결제 진행하면 된다.

Initialize this repository with a README 는 repository에 README 파일을 생성할지 선택하는 것으로 체크해서 진행해보자.

Add.gitignore: 는 어떤 유형의 파일(ex .cache , \__init__)은 git으로 관리하지 않고 무시하겠다는 설정을 말하는데 차후에 필요에 따라 설정하기로 하고, None 으로 세팅하자.

Add a license: 내가 올린 파일들의 license를 어떻게 설정할지 정하는 것이다. 복제해서 상업용으로 써도되는지, 학술 연구나 비상업적인 목적으로만 써야되는지 등이 있는데, 목적에 맞게 설정하면 된다.  

<br>

##### 3) 로컬 저장소 만들기 (굳이 만들지 않고 기존 디렉토리(= 폴더)에서 진행해도 됩니다!)

현재 위치가 c:/users/myfolder 라고 한다면 새로운 디렉토리를 만들 곳으로 이동한다.

> c:/users/myfolder>cd c:/이동하고싶은/위치로/이동하세요        # cd : change directory 줄임말

> c:/users/myfolder>cd c:/dev      # 예시, c드라이브에 dev directory로 이동합니다.

> c:/dev>mkdir myproject      # mkdir : make directory 줄임말

> c:/dev>cd myproject      # dev directory에 방금 만들어진 하위 directory myproject로 이동

> c:/dev/myproject>**git init**      # git : git 명령어를 사용하겠다고 컴퓨터에 알려줌, init : initialize(초기화)한다는 뜻으로 myproject 라는 directory가 앞으로 내가 사용할 로컬 git 저장소라고 컴퓨터에게 알려줌, 이 때 myproject directory 안에 '숨겨진 파일' 하나가 만들어진다. (참고로 cmd창에서는 error가 발생하지 않으면 명령어가 정상적으로 동작한 것이다.)

<br>

##### 4) git에서 내 상태 확인 및 파일 하나 commit 하기

> c:/dev/myproject>**git status**      # 내가 어떤 branch 상에 있는지, 새로운 파일이나 수정된 파일이 있는지 확인해준다. 따로 branch 이동하지 않았으므로 master branch 위에 있을 것이다. 그리고 아직은 변경내용이 없으므로 commit 할 것이 없다. (commit이란? 데이터베이스에 어떤 변화를 준 내용을 영구적으로 확정한다는 명령이다. git도 데이터베이스의 일종이다.)

myproject directory에 메모장 파일이나 버전관리하고 싶은 소스코드 파일을 만들거나 외부에서 가지고 오자. 이후에 **git status**를 다시 입력하면, 새로운 파일이 들어왔다는 내용을 보여줄 것이다. 이때, 'Untracked files' 라고 하면서 <u>(경로가 포함된)파일명</u>이 화면에 보여지는데, 이는 git이 tracking(추적)하고 있지 않다는 것을 말한다. 그러면 이제 내가 새롭게 들여온 파일을 tracking 하게 만들어 주자!

> c:/dev/myproject>**git add** **해당 위치에 파일명을적어주세요**      # 참고로 myproject 하위 directory에 새로운 파일을 추가했다면 ex) posts/hello_git.txt 와 같이 하위 directory 경로를 포함한 파일명을 적어줘야 한다. 

**git add 파일명** 입력한 뒤 다시 **git status** 입력하면 new file: 이라는 곳에 추가한 파일명이 보일 것이다. 다음으로 git add한 내용을 로컬 컴퓨터가 영구적으로 기억할 수 있도록 commit할 것이다.

> c:/dev/myproject>**git commit -m "여기에는 어떤 변경내용이 있었는지 적어줍니다"**      # -m 은 뒤따르는 텍스트는 메시지로 읽어야 한다고 알려주는 것이고, 이는 이후 파일 버전의 변경내용, 이유 등에 대한 summary 역할을 해준다.

<br>

##### 5) 로컬 저장소와 GitHub 저장소 연결하기

우린 아직 로컬 컴퓨터와 원격 저장소(GitHub)를 연결해주지 않았다. 이제 연결하자!

> c:/dev/myproject>**git remote add origin https://github.com/깃헙유저이름/repository이름.git**      # remote(원격지에) add(git 저장소 추가하려는데) origin(위치는) https://~~ 주소로 하겠다 정도로 이해하고 넘어가자.

> c:/dev/myproject>**git remote -v**      #  -v : verbose(장황한, 상세한)의 줄임말, 여기서는 로컬 저장소가 통신할 원격 저장소가 어떤 것인지 보여준다. remote 설정해준 github 주소가 뜰 것이다.

##### 6) 로컬 저장소에 저장된 변경사항(commit 했던 내용들)을 GitHub 으로 업로드 하기

push를 진행하기 앞서 선행되어야 할 것은 로컬에서 추가/수정한 변경 내용을 commit 해야 한다. 이를 하지 않으면, 로컬에서 변경한 내용이 확정되지 않은 상태이므로 원격으로 보낼 변경 내용이 없기 때문이다.

> c:/dev/myproject>**git push**      # push: 로컬에서 commit한 내용 원격으로 보내줘라

위 명령으로 실행되지 않으면, **git push origin master** 를 입력해보자.

또는 **git psuh --set-upstream origin master** 를 입력하고 나면, **git push**가 될 것이다.

<br>

<br>

이정도로 일단락하고 branch 가 어떤 개념인지 pull, merge 등에 대해서는 추후 보완하겠다.

To be contiune...

