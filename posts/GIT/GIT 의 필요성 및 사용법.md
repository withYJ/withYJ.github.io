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



GIT 개념은 아래 링크를 보며 추가적으로 이해해 나가면 좋을 것 같다.

https://rhostem.github.io/posts/2017-01-07-git-basic/  



GitHub 은 Local에서 작업한 Git의 내용을 원격으로 저장할 저장소 역할을 하는 공간이다.  





### 1. GIT 설치 & 업데이트 - Windows 기준

1) 아래 링크에서 자신의 OS 환경에 맞게 다운로드 한다.

https://git-scm.com/downloads  



2) 설치 옵션은 Windows 의 경우 아래 참고하면 된다.

http://igotit.tistory.com/entry/Git-%EC%9C%88%EB%8F%84%EC%9A%B0%EC%9A%A9-%EC%84%A4%EC%B9%98  



3) 이미 설치되어 있고 업데이트가 필요하다면 cmd 창에서(Windows 키 + r 눌러서 cmd 입력하면  cmd 창 열림) 아래와 같이 입력한다.  

>  c: ~ ~ >git --version						# git version 확인

> c: ~ ~ >git update-git-for-windows			# git 최신 버젼 다운로드 및 설치 진행

말이 업데이트지 새버전 설치하는 것이랑 같기 때문에 설치 옵션 재설정 해줘야 하고, 이는 2) 를 참고하면 된다.  

참고) mac 의 경우 update 진행 방법 https://medium.com/@katopz/how-to-upgrade-git-ff00ea12be18  





### 2. Git 사용 및 GitHub에 파일 올려보기

1) user.name , user.email 초기 설정하기

cmd 창에 아래와 같이 입력해 보자.

> c: ~~ >git config --global user.name		# 현재 로컬 컴퓨터에 설정된 git user.name 조회

> c: ~~ >git config --global user.email		# 현재 로컬 컴퓨터에 연동된 github email 조회  



처음 설치하면 아무것도 설정되어 있지 않을 것이다. 이제 설정해보자.

> c: ~~ >git config --gobal user.name "여기에 이름을 설정해 주세요"

> c: ~~ >git config --global user.email "여기에 GitHub가입에 사용한 이메일 주소를 적어주세요"  



2) 온라인 저장소 만들기 (이미 GitHub에서 repository 만드신 분은 점프하세요!)

![Alt text](/images/git1_1.png)



눌리고 들어가면 우측 상단에 **NEW** 를 눌러주고 repository를 만든다. (아래는 예시)

![Alt text](/images/git1_2.png)

Repository name은 프로젝트 명이나 각자의 목적에 맞게 적어주면 된다. 최상위 폴더명이라 생각하면 쉽게 이해될 것 같다.

Description은 Repository 내용에 대한 간단한 소개글이라 생각하면 된다. (선택사항임)

Public 으로 설정하, Private 사용하고 싶으면 유료결제 진행하면 된다.

Initialize this repository with a README 는 repository에 README 파일을 생성할지 선택하는 것으로 체크해서 진행해보자.

Add.gitignore: 는 어떤 유형의 파일(ex .cache , \__init__)은 git으로 관리하지 않고 무시하겠다는 설정을 말하는데 차후에 필요에 따라 설정하기로 하고, None 으로 세팅하자.

Add a license: 내가 올린 파일들의 license를 어떻게 설정할지 정하는 것이다. 복제해서 상업용으로 써도되는지, 학술 연구나 비상업적인 목적으로만 써야되는지 등이 있는데, 목적에 맞게 설정하면 된다.  



To be contiune...

