### Data Structure

### 데이터 구조
- 여러 데이터를 효과적으로 사용, 관리하기 위한 구조(str, list, dict 등)
### 자료구조
- 컴퓨터 공학에서는 '자료 구조'라고 함
- 각 데이터의 효율적인 저장, 관리를 위한 구조를 나눠 놓은 것
#### 데이터 구조 활용
- 문자열, 리스트, 딕셔너리 등 각 데이터 구조의 메서드를 호출하여 다양한 기능을 활용하기
### 메서드
- 객체에 속한 함수
- 객체의 상태를 조작하거나 동작을 수행
- 메서드는 클래스(class) 내부에 정의되는 함수
- 클래스는 파이썬에서 '타입을 표현하는 방법'이며 이미 은연중에 사용해왔음
- 예를 들어 help 함수를 통해 str을 호출해보면 class였다는 것을 확인 가능
- 메서드는 어딘가(클래스)에 속해 있는 <span style='color:orange;'>함수</span>이며, 각 데이터 타입별로 다양한 기능을 가진 메서드가 존재
## 시퀀스 데이터 구조
### 문자열
|        메서드      	|                                         설명                                        	|               예시              |
|:------------------:	|:-----------------------------------------------------------------------------------:	|:----------------------------:|
|      s.find(x)     	|     x의   첫 번째 위치를 반환. 없으면,   -1을 **반환**                                	|   `print('banana'.find('a')) # 1`
|      s.index(x)    	|     x의   첫 번째 위치를 반환. 없으면,   **오류** 발생                                  	|   `print('banana'.index('a'))`
|     s.isupper()    	|     대문자 여부                                                                     	| ` string1 = 'HELLO' print(string1.isupper()) # True`
|     s.islower()    	|     소문자 여부                                                                   	| ` string1 = 'HELLO'  print(string1.islower()) # False`
|     s.isalpha()    	|     알파벳 문자 여부      *단순 알파벳이 아닌 유니코드 상 Letter (한국어도 포함)    	|   `string1 = 'Hello'   print(string1.isalpha()) # True`

파이썬 is = 뭐가 있냐없냐같은 것이기 때문에 결과값이 모두 T/F로 나뉨
이런 이유로 우리가 개인적으로 만든 함수도 T/F가 반환되면 is로 짓는게 좋음

#### 문자열 조작 메서드 (새 문자열 반환)
|                  메서드                 	|                                              설명                                            	|
|:---------------------------------------:	|:--------------------------------------------------------------------------------------------:	|
|      <span style="color:orange"> s.replace(old,   new[,count]) </span>    	|    <span style="color:orange"> 바꿀 대상 글자를 새로운 글자로 바꿔서 반환 </span>                                              	|
|            <span style="color:orange"> s.strip([chars]) </span>           	|    <span style="color:orange"> 공백이나 특정 문자를 제거 </span>                                                               	|
|    <span style="color:orange"> s.split(sep=None,   maxsplit=-1) </span>   	|    <span style="color:orange"> 공백이나 특정 문자를 기준으로 분리 </span>                                                      	|
|      <span style="color:orange"> 'separator'.join(iterable) </span>     	|    <span style="color:orange"> 구분자로 iterable의 문자열을 연결한 문자열을 반환 </span>                                          |
|              s.capitalize()             	|     가장   첫 번째   글자를   대문자로   변경                                                	|
|                 s.title()               	|     문자열 내 띄어쓰기 기준으로 각 단어의 첫 글자는 대문자로,      나머지는 소문자로 변환    	|
|                 s.upper()               	|     모두   대문자로 변경                                                                     	|
|                 s.lower()               	|     모두   소문자로 변경                                                                     	|
|               s.swapcase()              	|     대↔소문자 서로 변경                                                                      	|

### 리스트
#### 리스트 값 추가 및 삭제 메서드
|          메서드         	|                                                   설명                                                  	|
|:-----------------------:	|:-------------------------------------------------------------------------------------------------------:	|
|        <span style="color:orange">L.append(x)</span>      	|     <span style="color:orange">리스트   마지막에 항목 x를   추가</span>                                                                   	|
|        <span style="color:orange">L.extend(m)</span>      	|     <span style="color:orange">Iterable m의   모든 항목들을 리스트 끝에 추가 (+=과   같은 기능) </span>                                   	|
|     L.insert(i,   x)    	|     리스트   인덱스 i에 항목 x를 삽입                                                                   	|
|        L.remove(x)      	|     리스트   가장 왼쪽에 있는 항목(첫 번째)   x를   제거     항목이 존재하지 않을 경우,   ValueError    	|
|          <span style="color:orange">L.pop()</span>        	|     <span style="color:orange">리스트   가장 오른쪽에 있는 항목(마지막)을   반환 후 제거</span>                                           	|
|         <span style="color:orange">L.pop(i)</span>        	|     <span style="color:orange">리스트의 인덱스 i에   있는 항목을 반환 후 제거 </span>                                                     	|
|         L.clear()       	|     리스트의 모든 항목 삭제                                                                             	|
#### 리스트 탐색 및 정렬 메서드
|               문법              	|                                   설명                                 	|
|:-------------------------------:	|:----------------------------------------------------------------------:	|
|     L.index(x)    	|     리스트에   있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환    	|
|            L.count(x)           	|     리스트에서 항목   x의 개수를 반환                                  	|
|            <span style="color:orange">L.reverse()</span>          	|     <span style="color:orange">리스트의 순서를 역순으로 변경 (**정렬 X**)</span>|
|             <span style="color:orange">L.sort()</span>            	|     <span style="color:orange">리스트를 정렬 (매개변수   이용가능)</span>  

#### 문자 유형 판별 메서드
#### 문자열에 포함된 문자들의 유형을 판별하는 메서드
- `isdecimal()`
    - 문자열이 모두 숫자 문자(0~9)로만 이루어져 있어야 True
- `isdigit()`
    - isdecimal()과 비슷하지만, 유니코드 숫자도 인식 ('①’ 도 숫자로 인식)
- `isnumeric()`
    - isdigit()과 유사하지만, 몇 가지 추가적인 유니코드 문자들을 인식 <br>(분수, 지수, 루트 기호도 숫자로 인식)
 `isdecimal()` ⊆ `isdigit()` ⊆ `isnumeric()`

|     isdecimal()    	|     isdigit()    	|     isnumeric()    	|                  예시                	|
|:------------------:	|:----------------:	|:------------------:	|:------------------------------------:	|
|         True       	|        True      	|         True       	|       "038",   "੦੩੮",   "０３８"     	|
|        False       	|        True      	|         True       	|          "⁰³⁸", "🄀⒊⒏", "⓪③⑧"         	|
|        False       	|       False      	|         True       	|     "⅛⅘", "ⅠⅢⅧ", "⑩⑬㊿", "壹貳參"    	|
|        False       	|       False      	|        False       	|          "abc", "38.0", "-38"        	|
