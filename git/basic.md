# Github 특강 - Basic

## git이란?

## git 설치

### 최초 설정

처음 컴퓨터에 git 설치하면, 사용자의 이메일과 이름을 적어준다. 이는 앞으로 일어나는 커밋에 서명을 하기 위해서 필요하다.

```
$ git config --glober user.name "<hongsinkang>"

$ git config --glober user.email "<hongsinkang>@<gmail.com>"
```

잘 설정되었나 확인하려면
```
$ git config user.name
이름 출력

$ git config user.email
이메일 출력
```



### 초기화

초기화는 `git init` 을 통해 진행한다.



### add 하기



### commit 하기



### log 보기



### 원격 저장소 등록하기



### 원격 저장소에 push하기



## branch

```touch home.md
git add home.md

git commit -m 'add home'

git branch about  # about 브랜치 생성

git switch about  # about 브랜치로 이동

git branch  # 현재 브랜치 현황 확인
```



## Summary

| 명령어                     | 설명                                               |
| -------------------------- | -------------------------------------------------- |
| `git init`                 | 빈 디렉토리(폴더)를 git 저장소(repo)로 초기화한다. |
| `git add <filename>`       | <filename> 을 Stage에 올린다                       |
| `git commit -m "filename"` | 커밋한다                                           |











