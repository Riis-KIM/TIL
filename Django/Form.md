### Form
- 유효성 검사 어려움
  - 유효성 검사를 구현하기 위해서는 입력 값, 형식, 중복, 범위, 보안 등 많은 것 고려 필요
- 사용자 입력 데이터를 수집하고, 처리 및 유효성 검사를 수행하기 위한 도구
  - 유효성 검사를 단순화하고 자동화 할 수 있는 긷능 제공
- new 함수 변경
- form 인스턴스 출력
#### Widgets
- HTML 'input' element의 표현을 담당
- 단순히 input 요소의 속성 및 출력되는 부분을 변경하는 것
### ModelForm
- form : 사용자 입력 데이터를 DB에 저장하지 않을 때
- ModelForm : 사용자 입력 데이터를 DB에 저장해야 할 때
- Meta class
  - ModelForm의 정보를 작성하는 곳
  - 'fields' 및 'exclude' 속성
    - exclude 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수 도 잇음
  - Django에서 ModelForm에 대한 추가 정보나 속성을 작성하는 클래스 구조를 Meta 클래스로 작성했을 뿐 파이썬 문법관점으로 접근하면 안됨
#### is_valid()
- 여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를 Boolean으로 반환
#### save()
- 데이터베이스 객체를 만들고 저장하는 ModelForm의 인스턴스 메서드
- 키워드 인자 instance 여부를 통해 생성할 지, 수정할 지 결정
  - instance 없으면 생성, 있으면 수정
#### new& creat 함수간 공통점과 차이점
- 공통점 : 데이터 생성을 구현하기 위함
- 차이점 : new는 GET 메서드만, create는 POST 메서드만