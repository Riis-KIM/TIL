### web
- web site, web application 등을 통해 사용자들이 정보를 검색하고 상호 작용하는 기술
- HTML
  - structure
  - HyperText Markup Language
  - 웹 페이지의 의미와 구조를 정의하는 언어
- CSS
  - styling
- 자바스크립트
  - behavior
#### Hypertext
- 웹 페이지를 다른 페이지로 연결하는 링크
- 비선형성 / 상호연결성 / 사용자 주도적 탐색
#### Markup language
- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
- 마크업을 한다 -> 구조를 만든다
#### HTML 구조
- ![사진](./images/HTML.png)
- ![사진](./images/HTML_head.png)
- 알트+B
- HTML Element: 하나의 요소에는 여는 태그와 닫는 태그 그리고 내용이 구성됨
  - <p></p>
- HTML Attribute: 사용자가 원하는 기준에 맞도록 요소 설정하거나 방식으로 동작 조절
  - 나타내고 싶지 않지만 추가적인 기능, CSS스타일 적용 위해 해당 요소 선택값
  1. 속성은 요소 이름과 속성 사이에 공백 필요
  2. 하나 이상의 속성들이 있는 경우에는 속성 사이 공백으로 구분
  3. 속성 값은 열고 닫는 따옴표로 감쌈 
#### CSS
- 웹 페이지의 디자인과 레이아웃을 구성하는 요소
- 인라인 스타일 : HTML요소 내 style 속성 값으로 작성
- 내부 스타일 : head 태그 안에 style 태그에 작성
- 외부 스타일 : 별도의 CSS파일 생성 후 HTML link 태그 사용해 불러옴
#### CSS selector 종류
- 기본 선택자
  - 전체(*) 선택자
    - HTML 모든 요소 선택
  - 요소(tag) 선택자
    - 지정된 모든 태그 선택
  - 클래스(class) 선택자
    - 주어진 클래스 속성을 가진 모든 요소 선택
  - 아이디(id) 선택자
    - 주어진 아이디 속성을 가진 요소 선택
    - 문서에는 아이디를 가진 요소가 하나만 있어야함
  - 속성(attr) 선택자 등
- 결합자
  - 자손 결합자(" "(space))
    - 첫 번째 요소의 자손 요소들 선택
    - ex) p span은 <p> 안에 있는 모든 <span>을 선택(하위 레벨 상관 없이)
  - 자식 결합자(">")
    - 첫 번째 요소의 직계 자식만 선택
    - ex) ul > li은 <ul> 안에 있는 모든 <li> 선택 (한단계 아래 자식들만)
#### 명시도
- CSS selector에 가중치 계산해 어떤 스타일 적용할지 결정
- 동일한 요소를 가진 2개 이상의 CSS 규칙이 있을 경우 명시도 높은 Selector 선택
- 한 요소에 동일한 가중치를 가진 선택자 적용 시 CSS 마지막에 나오는 선언 선택(계단식)

#### 명시도 순서
1. !important -> 계단식 구조 무시하고 강제로 스타일 적용해 사용을 권장하지는 않음
2. inline 스타일
3. 선택자
    - id 선택자 > class 선택자 > 요소 선택자
4. 소스 코드 선언 순서

#### CSS 상속
- 상속되는 속성
  - Text 관련 요소(font, color, text-align), opacitym visibility 등
- 상속되지 않는 속성
  - Box model 관련 요소(width, height, border, box-sizing)
  - position 관련 요소(position, top/right/bottom/left, z-index)

#### CSS box model
- 웹 페이지의 모든 HTML 요소를 감싸는 사각형 상자 모델
- 내용, 안쪽 여백, 테두리, 외부 간격으로 구성되어 요소의 크기와 배치를 결정
- 박스 표시 타입
  - Outer display type
    - 박스가 문서 흐름에서 어떻게 동작할지를 결정, block, inline
#### block 특징
- 항상 새로운 행으로 나뉨
- width와 height 속성 사용 가능
- padding, margin, border로 인해 다른 요소를 상자로부터 밀어냄
  - Inner display type

#### 박스 구성요소
- content box
  - 실제 콘텐츠가 표시되는 영역 크기
  - width 및 height 속성을 사용하여 크기 조정
- padding box
  - 콘텐츠 주위에 공백
  - padding 관련 속성을 사용하여 크기 조정
- border box
  - 콘텐츠와 패딩을 래핑
  - border 관련 속성을 사용해 크기 조정
- margin box
  - 콘텐츠, 패딩 및 테두리 래핑
  - 박스와 다른 요소 사이의 공백
  - margin 관련 속성 사용해 크기 조정

#### shorthand 속성
- border
  - border-width, border-style, border-color 마음대로 저장
- margin & padding
- 4개 - 상우하좌
- 3개 - 상/좌우/하
- 2개 - 상하/좌우
- 1개 - 공통

#### inline-box
- inline과 block요소 사이의 중간 지점을 제공하는 display 값
- width 및 height 속성 사용 가능
- padding, margin 및 border로 인해 다른 요소가 상자에서 밀려남
- 새로운 행으로 넘어가지 않음

#### CSS layout
- 각 요소의 위치와 크기를 조정하여 웹 페이지의 디자인을 결정하는 것
- display, position, flexbox
- CSS position
  - 요소를 normal flow에서 제거하여 다른 위치로 배치하는 것
#### position
- 목적
  - 전체 페이지에 대한 레이아웃을 구성하는 것보다는 페이지 특정 항목의 위치를 조정하는 것
- static
  - 요소를 normal flow에 따라 배치
  - top, right, bottom, left 속성이 적용되지 않음
  - 기본값
- relative
  - 요소를 normal flow에 따라 배치
  - 자신의 원래 위치를 기준으로 이동
  - top, right, bottom, left 속성으로 위치 조정
  - 다른 요소의 레이아웃에 영향을 주지 않음
- absolute
  - 
- fixed
  - 요소를 normal flow에서 제거
  - 현재 화면영역을 기준으로 이동
  - 스크롤해도 항상 같은 위치에 유지됨
  - top, right, bottom, left 속성으로 위치를 조정
  - 문서에서 요소가 차지하는 공간이 없어짐
- sticky
  - relative 와 fixed가 합쳐짐
#### z-index 특징
- 기본값은 auto
- 부모 요소의 z-index 값에 영향 받음
- 같은 부모 내에서만 z-index 값을 비교
- 부모의 z-index가 낮으면 자식의 z-index가 아무리 높아도 부모보다 높게 못감
- 같을 경우 나중에 작성된 코드가 위로 올라감
#### CSS Flexbox
- 요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식

flexbox 슉성 목록
- flex container 관련 속성
- flex item 관련 속성
- flex item은 기본적으로 행으로 나열
- flex-direction
  - flex item이 나열되는 방향 정리
  - flex item 목룍이 flex contaioner에
  - flex-wrap
  - justify-content
    - 주 축을 따라 flex item과 주위에 공간을 분배
  - align-content
- justify, content 차이
### Bootstrap
### CDN
#### Bootstrap 사용법
- {property}{sides}-{size}
- size는 rem을 사용 
- mx-auto --(block박스 가운데 정렬하기 위해)
- bootsrap은 공식 문서를 켜놓고 보면서 해야함
#### Reset CSS
- 모든 HTML 요소 스타일을 일관된 기준으로 재설정하는 간결하고 압축된 규칙 세트
- HTML element, Table, List 등의 요소들에 일관성 있게 스타일을 적용시키는 기본 단계
- 모든 브라우저는 각자의 'user agent stylesheet'를 가지고 있음
  - 웹사이트를 보다 읽기 편하게 하기 위해
- 문제는 이 설정이 각 브라우저마다 다름
- 모든 브라우저에서 웹사이트를 동일하게 보이게 만들어야 하는 개발자를 위해
- 모두 똑같은 스타일 상태로 만들고 개발을 시작
#### Normalize CSS
- Reset CSS 방법 중 대표적인 방법
- 웹 표준 기준으로 브라우저 중 하나가 불일치 한다면 차이가 있는 브라우저를 수정
#### component
#### semantic web
- 웹 데이터를 의미론적으로 구조화된 형태로 표현하는 방식
- HTML에서
  - 단순이 제목처럼 보이게 큰 글자로 만들기
  - 페이지 내 최상위 제목이라는 의미를 제공하는 요소 h1
- 기본적인 모양과 기능 이외에 의미를 가지는 HTML 요소
  - 검색엔진 및 개발자가 웹 페이지 콘텐츠를 이해하기 쉽도록
#### CSS 방법론
- css를 효율적이고 유지 보수가 용이하게 작성하기 위한 일련의 가이드라인
- OOCSS
  - 객체 지향적 접근법을 적용하여 CSS를 구성하는 방법론
  - 구조와 스킨을 분리
  - 컨테이너와 콘텐츠 분리 

### 이미지의 역할
1. 컨텐츠 (img 태그)
2. 단순 배경 (background-img)


#### Bootstrap Grid system
- 웹 페이지의 레이아웃을 조정하는 데 사용되는 12개의 컬럼으로 구성된 시스템
- 반응형 디자인을 지원해 웹 페이지를 모바일, 태블릿, 데스크탑 등 다양한 기기에서 적절하게 표시할 수 있도록 도움
#### Grid system 구조
- container
  - column들을 담고 있는 공간
- column
  - 실제 컨텐츠를 포함하는 부분
- gutter
  - 컬럼과 컬럼 사이의 여백 영역
- 1개의 row 안에 12개의 column 영역이 구성
  - 각 요소는 12개 중 몇 개를 차지할 것인지 지정됨

#### 반응형 웹 디자인
- 디바이스 종류나 화면 크기에 상관없이, 어디서든 일관된 레이아웃 및 사용자 경험을 제공하는 디자인
- 브레이크 포인트
  - 웹 페이지를 다양한 화면 크기에서 적절하게 배치하기 위한 분기점
  - 화면 너비에 따라 6개의 분기점 제공(xs, sm, md, lg, xl, xxl)
  - 각 breakpoints마다 설정된 최대 너비 값 "이상으로" 화면이 커지면 grid system 동작이 변경됨
- css 레이아웃 기술들은 각각 고유한 특성과 장단점을 가지고 있음
- 서로 상호보완적이며, 특정 상황에 따라 적합한 도구 다름
- 최적의 기술 선택하고 효과적으로 활용하기 위해선 실제 개발 경험 필요
#### UI&UX
- UX
  - 제품이나 서비스를 사용하는 사람들이 느끼는 전체적인 경험과 만족도를 개선하고 최적화하기 위한 디자인과 개발 분야

검색엔진 최적화(SEO)
seobility

### 시멘틱 구조
<header> - 문서의 머릿말
<nav> - 페이지 메뉴
<main> - 주요 콘텐츠
<section> - 주제별로 문서의 콘텐츠 영역
<article> - 개별 콘텐츠 요소
<footer> - 문서의 꼬리말

1. bootstrap -> 다른 사람 코드 가져오는 법 -> 설치 or 실시간으로 가져오자(CDN)
2. font -> 구글폰트
3. 아이콘 -> fontawesome

cdnjs.com
