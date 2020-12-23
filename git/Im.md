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