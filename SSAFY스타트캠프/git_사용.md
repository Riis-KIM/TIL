# Git이란
  ## Git : 분산 버전 관리 시스템  
  분산 -> 버전을 여러 개의 복제된 저장소에 저장함(서버, 개인 컴퓨터 등)  
  버전 관리 ->  변화를 기록하고 추적함, 각 버전은 이전 버전에서 변경된 **변경사항**만 가지고 있음  
  ### 장점
  - 코드의 버전을 관리하기 유용함
  - 개발되어 온 과정을 파악하기 쉬움
  - 중앙 서버에 의존하지 않고 동시에 작업 수행 가능해 생산성 향상
  - 중앙 서버의 장애, 손실을 대비하기 쉬움
  - 인터넷이 연결되지 않는 환경에서도 개발 가능, 이후 한번에 변경사항을 업로드 하면됨
  ### 3가지 영역
  - Working directory : 실제 작업중인 파일들이 위치하는 영역
  - staging area : working directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가. 제외하는 중간 준비 영역
  - repository : 버전*(commit)* 이력과 파일들이 영구적으로 저장되는 영역
---
# Git 코드
### 로컬 저장소
- `git init`
  - 로컬 저장소 설정(초기화)
  - 깃의 버전 관리를 시작할 디렉토리에서 진행
  - **깃 저장소 내부에 또 다른 저장소가 존재하면 안됨**
  - *복구 하려면 .git 이라는 숨겨진 파일 삭제*
- `git status`
  - 현재 깃의 상태를 확인함, stating area와 repository의 상태는 눈으로 확인 불가능하니 해당 명령어를 이용해 확인
- `git add`
  - 파일의 변경 내용을 Working directory에서 staging area로 옮길 때 사용하는 명령어
  - `git add .` 사용시 해당 폴더 내의 모든 변경사항을 옮김
  - `git add 파일명` 사용시 해당 파일의 변경사항만 옮김 
- `git commit`
  - stating area에 존재하는 내용을 repository로 옮김, 해당 시점의 버전을 생성하고 변경 이력을 남김
  - `git commit -m "내용"` 을 통해 해당 commit이 어떤 뜻인지 메세지를 남길 수 있음
- `git log`
  - repository에 올라간 내용은 status로 확인할 수 없기 때문에 사용하는 명령어
  - 최신 내용이 가장 위에 올라와 있음
  - `git log --oneline`을 통해 한 줄로 내용을 확인 할 수 있음
- `gitignore`
  - `.ignore` 파일을 만들고 git을 사용하지 않을 내용을 적으면 됨, 작성 시 특정 파일이나 디렉토리를 추적하지 않도록 설정
  - **깃에 한번도 commit되지 않은 파일만 적용가능**
  - 실수로 넣는다면 `git rm —cached` 명령어 통해 git 캐쉬 삭제 필요
### 원격 저장소
- `git config —global`
  - `git config --global user.email 이메일`
  - `git config --global user.name 이름`
  - 위 두가지 내용을 통해 자신의 이름과 이메일을 매번 입력하지 않도록 저장함
- `git remote`
  - `git remote add origin remote_repo_url` 해당 저장소의 이름과 URL을 지정
  - `git remote -v`잘 되었는지 확인에 사용
- `git push`
  - 변경된 사항들만 올라감, commit된 내용이 없으면 실행되지않음
- `git pull`
  - 추가적으로 commit된 내용을 가져옴
- `git clone`
  - 모든 내용(파일 등)을 전부 가져옴, 다운로드와 비슷함
  - `git clone remote_repo_url`원격 저장소를 전부 복제해 오는것으로 해당 명령어 사용 시 `git init`명령을 통해 git 저장소 지정해줄 필요없음
---
---
- `git revert`
  - 특정 commit을 없던 일로 만드는 작업
  - 프로젝트 기록에서 commit을 없었던 일로 처리 후 그 결과를 새로운 commit으로 추가
  - 기록을 남겨 저장을 하고 다른 개발자들과 진행사항을 맞추기 위해서
  - 삭제된 commit은 없어지는것이 아니라 반영이 안될뿐
  - `git revert aaaa bbbb` : 여러 commit을 한번에 취소
  - `git revert aaaa .. dddd` : 범위 내 commit을 한번에 취소
  - `git revert --no-edit` : vim 실행하지 않고 취소
  - `git revert --no-commit` : 자동으로 commit하지 않고 변경 사항을 staging area에 올림
- `git reset`
  - 특정 commit으로 되돌아가는 작업
  - `git reset [옵션] <commit id>`
  - 특정 commit으로 되돌아가는데 덮어쓰는 방식으로 돌아가기 때문에 특정 시점 이후의 commit을 전부 삭제 **위험함**
  - `--soft` = 삭제한 내용을 staging area에
  - `--mixed` = 삭제된 내용을 working directory(기본값)
  - `--hard` = 기록 안남기고 아예 삭제

### *부록*
- `git undoing`
  - 파일 내용을 수정 전으로 돌리는 행위
  - staging area에 올라간 파일을 unstage함
- `git restore`
  - modified 상태의 파일 되돌리기
  - working directory에서 파일을 수정한 뒤, 수정 내용을 전부 초기화 하는 작업
  - 원래 파일로 덮어쓰는 방식이라 수정 내용 전부 삭제
  - 해당 명령어 사용 시 이후 수정 취소 후 내용 복원 X
- `git unstage`
  - `git rm --cached` staging area에서 working directory로 되돌리기 // git 저장소에 commit이 없을 때 사용
  - `git restore --staged` staging area에서 working directory로 되돌리기 // git 저장소에 commit이 존재할때 사용