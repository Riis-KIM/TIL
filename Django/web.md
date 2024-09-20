Django 사용하는 이유
- 다양성
  - python 기반으로 웹, 모바일 앱 백엔드, API 서버 및 빅데이터 관리 등 광범위한 서비스 개발에 적합
- 확장성
  - 대량의 데이터에 대해 빠르고 유연하게 확장할 수 있는 기능 제공
- 보안
  - 취약점으로부터 보호하는 보안 기능이 기본적으로 내장
- 커뮤니티 지원
  - 개발자를 위한 지원, 문서 및 업데이트 제공함
#### 디자인 패턴
- 소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책
  - 어플리케이션의 구조는 이렇게 구성하자라는 관행
#### MVC 디자인 패턴(Model, View, Controller)
- 애플리케이션을 구조화하는 대표적인 패턴
  - 데이터 & 사용자 인터페이스 & 비즈니스 로직을 분리
  - 시각적 요소와 뒤에서 실행되는 로직을 서로 영향 없이, 독립적이고 쉽게 유지보수할 수 있는 앱을 만들기 위함
#### MTV 디자인 패턴(Model, Template, View)
- Django에서 앱을 구조화하는 패턴
  - 기존 MVC 패턴과 동일하나 단순히 명칭을 다르게 정의함
  - View -> Template, Controller -> View
####
- Django project
  - 애플리케이션의 집합
    - DB 설정, URL 연결, 전체 앱 설정 등을 처리
- Django application
  - 독립적으로 작동하는 기능 단위 모듈
    - 각자 특정한 기능을 담당하며 다른 앱들과 함께 하나의 프로젝트를 구성

#### 환경 시작
1. venv 가상환경 설정
   1. python -m venv venv
2. 활성화 필요
   1. source venv/Scripts/activate
3. .gitignore 생성
4. 프로젝트 생성
   1. django-admin startproject /// .
5. 서버 활성화로 잘 생성되었는지 확인
   1. python manage.py runserver
   2. ctrl + c로 종료
6. 아티클 생성
   1. python manage.py startapp articles
   2. 프로젝트 -> settings.py -> INSTALLED_APPS -> articles 추가

#### 순서
1. urls.py
2. views.py
3. template
app/templates 고정


### Django Template System(DTL)
- 데이터 표현을 제어하면서, 표현과 관련된 부분을 담당
- template에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템
1. Variable
   - render 함수의 세번째 인자로 딕셔너리 데이터를 사용
   - 딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
   - dot을 사용해 변수 속성에 접근할 수 있음
2. Filters
  - 표시할 변수를 수정할 때 사용(변수 + "|" + 필터)
  - chained이 가능하며 일부 필터는 인자를 받음
  - 약 60개의 built-in 템플릿 필터를 제공
3. Tags
  - 반복 또는 논리를 수행하여 제어 흐름을 만듦
  - 일부 태그는 시작과 종료 태그가 필요
  - 약 24개의 built-in 템플릿 태그 제공
4. Comments
  - {#name#}
  - {%comment%}

### 템플릿 상속
- 페이지의 공통요소를 포함하고, 하위 템플릿이 재정의 할 수 있는 공간을 정의하는 기본 'skeleton' 템플릿을 작성하여 상속 구조를 구축
#### 'extends' tag
- 자식(하위)템플릿이 부모 템플릿을 확장한다는 것을 알림
- 반드시 자식 템플릿 최상단에 작성되어야 함
#### 'block' tag
- 하위 템플릿에서 재정의 할 수 있는 블록을 정의
- 상위 템플릿에 작성하며 하위 템플릿이 작성할 수 있는 공간을 지정
- endblock까지도 이름을 지정해줘야함
#### 'form' element
- 사용자로부터 할당된 데이터를 서버로 전송
#### 'action' & 'method'
- action
  - 입력 데이터가 전송될 URL을 지정 (목적지)
  - 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐
- method
  - 데이터를 어떤 방식으로 보낼 것인지 정의
  - 데이터의 HTTP request methods (GET, POST)를 지정
#### 'input' element
- 사용자의 데이터를 입력 받을 수 있는 요소
- type 속성 값에 따라 다양한 유형의 입력 데이터를 받음
- 'name' attribute
  - input의 핵심 속성
  - 사용자가 입력한 데이터에 붙이는 이름(key)
  - 데이터를 제출했을 때 서버는 name 속성에 설정된 값을 통해서만 사용자가 입력한 데이터에 접근할 수 있음
#### Query String Parameters
- 사용자의 입력 데이터를 URL 주소에 파라미터를 통해 서버로 보내는 방법
- 문자열은 앰퍼샌드('&')로 연결된 key=value 쌍으로 구성되며, 기본 URL과는 물음표("?")로 구분됨
#### HTML request 객체
- form으로 전송한 데이터 뿐만 아니라 Django로 들어오는 모든 요청 관련 데이터가 담겨있음

### Django Model
- DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공
  - 테이블 구조를 설계하는 청사진
- django.db.models 모듈의 Model이라는 부모 클래스를 상속받음
  - 개발자는 가장 중요한 테이블 구조를 어떻게 설계할지에 대한 코드만 작성하도록 위한 것(상속을 활용한 프레임워크의 기능 제공)
- 클래스 변수명
  - 테이블의 각 "필드(열) 이름"
- Model Field
  - 데이터베이스 테이블의 열(column)을 나타내는 중요한 구성 요소
  - "데이터의 유형"과 "제약 조건"을 정의
### Model Field
- DB 테이블의 필드(열)을 정의하며, 해당 필드에 저장되는 데이터 타입과 제약조건을 정의
1. Field types (필드 유형)
  - 데이터베이스에 저장될 "데이터의 종류"를 정의
  1. CharField()
    - 제한된 길이의 문자열을 저장(max_length는 필수 옵션)
  2. TextField()
    - 길이 제한이 없는 대용량 텍스트를 저장(무한대는 아니고 사용하는 시스템에 따라 달라짐)

2. Field options (필드 옵션)
  - 필드의 동작과 제약조건을 정의
  - null
    - 데이터베이스에서 NULL값을 혀용할지 여부를 결정 (기본값:False)
  - blank
    - form에서 빈 값을 허용할지 여부를 결정 (기본값:False)
  - default
    - 필드의 기본값을 설정

#### 제약 조건 Constraint
- 특정 규칙을 강제하기 위해 테이블의 열이나 행에 적용되는 규칙이나 제한사항
  - ex) 숫자만 저장되도록, 문자가 100자까지만 저장되도록 하는 등

#### Migrations
- model 클래스의 변경사항(필드 생성, 수정 삭제 등)을 DB에 최종 반영하는 방법
- python manage.py makemigrations
- python manage.py migrate
- 1. model class 변경
- 2. makemigrations
- 3. migrate
- model class에 변경사항(1)이 생겼다면 반드시 새로운 설계도를 생성(2)하고, 이를 DB에 반영(3)해야 한다.

#### automatic admin interface
- Django가 추가 설치 및 설정 없이 자동으로 제공하는 관리자 인터페이스
  - 데이터 확인 및 테스트 등을 진행하는데 매우 유용
- 1. 어드민 계정 생성
  - python manage.py createsuperuser
- 2. admin에 모델 클래스 등록
  - admin.py에 작성한 모델 클래스를 등록해야만 admin site에서 확인 가능
  - from .models import Article
  - admin.site.register(Article)

#### 참고
- 데이터베이스 초기화
  - 1. migration 파일 삭제
  - 2. db.sqlite3 파일 삭제
  - ** __init__.py, migrations폴더 삭제 금지 **