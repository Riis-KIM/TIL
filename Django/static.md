### Static Files 정적 파일
- 서버 측에서 변경되지 않고 고정적으로 제공되는 파일
- 웹 서버의 기본동작은 특정 위치(URL)에 있는 자원을 요청(HTTP request)받아서 응답(HTTP response)을 처리하고 제공하는 것
- 이는 자원에 접근 가능한 주소가 있음이라는 의미
- 웹서버는 요청받은 URL로 서버에 존재하는 정적 자원을 제공함
  - 정적 파일을 제공하기 위한 경로가 있어야함
#### Static files 기본 경로
- app폴더/static/
- base.html에서 load static을 한다면 자식 템플릿에서 적용이 안된다
- load static을 작성한 html파일에서만 사용 가능
#### Static files 추가 경로
- STATICFILES_DIRS에 문자열 값으로 추가 경로 설정
- 정적 파일의 기본 경로 외에 추가적인 경로 목록을 정의하는 리스트
### Media filses
#### ImageField()
- 이미지 업로드에 사용하는 모델 필드
  - 이미지 객체가 직접 DB에 저장되는 것이 아닌 미지 파일의 경로 문자열이 저장됨
#### 준비사항
1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정
    - 미디어 파일들이 위치하는 디렉토리의 절대 경로, MEDIA_ROOT에서 제공되는 미디어 파일에 대한 주소를 생성(STATIC_URL과 동일한 역할)
2. 작성한 MEDIA_ROOT와 MEDIA_URL에 대한 URL 지정