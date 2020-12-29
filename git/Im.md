# git -intermediate



## Branch

```touch home.md
git add home.md

git commit -m 'add home'

git branch name  # name 브랜치 생성

git switch name  # name 브랜치로 이동

	# git switch -c name # name 브랜치를 생성하며 이동

git branch  # 현재 브랜치 현황 확인
```





### 브랜치 생성하기 (`git branch <name> `)

### 브랜치 확인하기 (`git branch`)

### 브랜치 옮기기 (HEAD 움직이기 `git switch`)

### 브랜치 합치기 (`git merge`)

항상 master에서 다른 브랜치를 병합한다.

### 브랜치 삭제하기 (`git branch -d <name>` )

# 

## Branch

| 명령어                            | 설명                                                    |
| --------------------------------- | ------------------------------------------------------- |
| `$ git branch <name>`             | 브랜치 생성                                             |
| `$ git branch`                    | 현재 브랜치 현황 확인                                   |
| `$ git switch <name>`             | 브랜치 이동(head 이동)                                  |
| `$ git switch -c <name>`          | 브랜치 생성 후 이동                                     |
| `$ git merge <name>`              | 브랜치 현재 위치에서 흡수 합병<br />(항상 master에서!!) |
| `$ git branch -d <name>`          | 브랜치 삭제                                             |
| `$ git branch -m <name1> <name2>` | name1을 name2로 이름변경                                |



## vim

```
$ vim <filename>              # vim 프로그램 실행
```

| 기능키 | 설명                        |
| ------ | --------------------------- |
| i      | insert                      |
| q      | quit                        |
| q!     | quit anyway                 |
| wq     | write & quit 저장 후 나가기 |



## Collaborating Project

### project 시작

github 실행 -> new repo 생성 -> 공유자 초대

```
$ mkdir ~/collab
$ cd collab
$ git init
$ touch README.md
"내용 수정 후 저장 (ctrl+s)"
$ git add .
$ git commit -m 'message'
$ git remote add origin <url>
$ git remote -v
$ git push origin master
```

공유 초대 받으면

```
$ git clone <url>                 # git 내 로컬에 복사

$ git pull origin master          # origin에 master 브랜치 데이터 가져오기
```

### conflict

```
vs code 실행
ctrl+` <=터미널 창 보기
기본 셸 설정 -> git bash
```

1. master에 바로 작업 X
2. 다른 브랜치 생성 후 작업 -> !!저장!! -> commit -> push
3. 승인 요청
4. master 변경 사항 pull



**새로운 환경에서 clone 부터

**항상 일어날 때 push 앉을 때 pull

**repo 있을 때 절대 git init 하지 말 것



## 불필요한 cash 관리

```
$ touch .gitignore 
```

[gitignore.io - Create Useful .gitignore Files For Your Project (toptal.com)](https://www.toptal.com/developers/gitignore)

쓰고 있는 프로그램 검색

-> 작성할 명령어 `.gitignore`에 복붙

**`.gitignore` 존재하는 폴더 내 모든 파일들 관리

```
$ git rm --cashed <filename>		# file cash 관리
$ git rm -r --cashed <foldername>	# folder cash 관리
```

