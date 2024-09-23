### ORM  (Object-Relational-Mapping)
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간의 데이터를 변환하는 기술
- Django와 DB간에 사용하는 언어가 다르기 때문에 소통 불가
- Django에 내장된 ORM이 중간에서 이를 해석
### QuerySet API
- ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는 데 사용하는 도구
  - API를 사용하여 SQL이 아닌 Python 코드로 데이터를 처리
#### Query
- 데이터베이스에 특정한 데이터를 보여 달라는 요청
- 쿼리문을 작성한다
  - 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성한다.
- 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변환하여 우리에게 전달
#### QuerySet
- 데이터베이스에게서 전달 받은 객체 목록(데이터모음)
  - 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음
- Django ORM을 통해 만들어진 자료형
- 단, 데이터베이스가 단일한 객체를 반환 할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환됨
- Queryset API는 python의 모델 클래스와 인스턴스를 활용해 DB에 데이터를 저장, 조회, 수정, 삭제하는 것
### CRUD
- 소프트웨어가 가지는 기본적인 데이터 처리 기능
- Create(저장)
- Read(조회)
- Update(갱신)
- Delete(삭제)
#### Queryset api 실습
1. 외부 라이브러리 설치
    - pip install django-extensions
    - setiings.py에 'django_extensions'추가
    - python manage.py shell_plus 실행
    - Django 환경 안에서 실행되는 python shell
- save()
  - 객체를 데이터베이스에 저장하는 인스턴스 메서드
#### Read()
- Return new QuerySets
  - all() : 전체 데이터 조회
  - filter() : 주어진 매개변수와 일치하는 객체를 포함하는 QuerySet 반환
- Do not return QeurySets
  - get() : 주어진 매개변수와 일치하는 객체를 반환
    - 객체를 찾을 수 없으면 DoesNotExist 예외를 발생시키고, 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생시킴
    - 위와 같은 특징을 가지고 있기 때문에 primary key와 같이 고유성(uniqueness)을 보장하는 조회에서 사용해야 함
#### update
- 인스턴스 변수를 변경 후 save 메서드를 호출
#### delete
- 삭제하려는 데이터 조회 후 delete 메서드 호출
### 참고
#### filter
- gt, gte, lt, lte = 초과, 이상, 미만, 이하
#### ORM, Query set 사용하는 이요
1. 데이터베이스 추상화
    - 개발자는 특정 데이터베이스 시스템에 종속되지 않고 일관된 방식으로 데이터를 다룰 수 있음
2. 생산성 향상
    - 복잡한 SQL 쿼리를 직접 작성하는 대신 Python 코드로 데이터베이스 작업을 수행할 수 있음
3. 객체 지향적 접근
    - 데이터베이스 테이블을 Python 객체로 다룰 수 있어 객체 프로그래밍의 이점을 활용할 수 있음