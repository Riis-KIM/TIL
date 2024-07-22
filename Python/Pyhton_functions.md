## Functions

### 함수 `Functions`

#### 개요
- 특정 작업을 수행하기 위한 재사용 가능한 코드 묶음

#### 함수를 사용하는 이유
- 두 수의 합을 구하는 함수를 정의하고 사용함으로써 코드의 중복을 방지
- <span style='color:red;'>재사용성</span>이 높아지고, 코드의 <span style='color:red;'>가독성과 유지보수성</span> 향상
- Docstring <- 함수 설명서 

### 함수의 구조
![image](https://github.com/ragu6963/TIL/assets/32388270/fe4bb4a9-f88d-43f8-9e6e-915e3c790b48)

#### 함수의 정의와 호출
- 함수 정의(정의)
    - 함수 정의는 `def` 키워드로 시작
    - def 키워드 이후 함수 이름 작성
    - 괄호안에 매개변수를 정의할 수 있음
    - 매개변수(parameter)는 함수에 전달되는 값을 나타냄

    ```python
    # 함수 정의
    def greet(name):
        """입력된 이름(name) 값에
        인사를 하는 메세지('Hello, ')를 만드는 함수
        """
        message = 'Hello, ' + name
        return message

    # 함수 호출 및 반환 값 할당
    result = greet('Alice')
    print(result)
    ```
- 함수 body
    - 콜론(`:`) 다음에 들여쓰기 된 코드 블록
    - 함수가 실행 될 때 수행되는 코드를 정의
    - Docstring은 함수 body 앞에 선택적으로 작성 가능한 함수 설명서
- 함수 반환 값
    - 함수는 필요한 경우 결과를 반환할 수 있음
    - `return` 키워드 이후에 반환할 값을 명시
    - `return` 문은 함수의 실행을 종료하고, 결과를 호출 부분으로 반환
  - return을 안붙여주면 파이썬이 알아서 `return None` 반환해줌
- 함수 호출
    - 함수를 사용하기 위해서는 호출이 필요
    - 함수의 이름과 소괄호를 활용해 호출
    - 필요한 경우 인자(argument)를 전달해야 함
    - 호출 부분에서 전달된 인자는 함수 정의 시 작성한 매개변수에 대입됨
    - 함수를 실행하기 위해 함수의 이름을 사용하여 해당 함수의 코드 블록을 실행하는 것

## 매개변수와 인자
#### 매개변수 `parameter`
- 함수를 정의할 때, 함수가 받을 값을 나타내는 변수

#### 인자 `argument`
- 함수를 호출할 때, 실제로 전달되는 값

#### 매개변수와 인자 예시
```python
def add_numbers(x, y): # x와 y는 매개변수(parameter)
    result = x + y
    return result


a = 2
b = 3
sum_result = add_numbers(a, b) # a와 b는 인자(argument)
print(sum_result)
```
### 다양한 인자 종류
#### Positional Arguments (위치인자)
- 함수 호출 시 인자의 위치에 따라 전달되는 인자
- <span style='color:crimson;'>위치인자는 함수 호출 시 반드시 값을 전달해야 함</span>/ 누락되면 안됨
#### Default Argument Values (기본 인자 값)
- 함수 정의에서 매개변수에 기본 값을 할당하는 것
- 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨
- 해당 위치에 새로운 인자를 넣어주면 새 인자값을 사용
####  Keyword Arguments (키워드 인자)
- 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
- 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음
- 인자의 순서는 중요하지 않으며, 인자의 이름을 명시하여 전달
- <span style='color:crimson;'>단, 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함</span>
#### Arbitrary Argument Lists (임의의 인자 목록)
- 정해지지 않은 개수의 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 <span style='color:red;'>`‘*’`</span>를 붙여 사용하며, 여러 개의 인자를 tuple로 처리
#### Arbitrary Keyword Argument Lists (임의의 키워드 인자 목록)
- 정해지지 않은 개수의 키워드 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 <span style='color:red;'>`‘**’`</span>를 붙여 사용하며, <br>여러 개의 인자를 dictionary로 묶어 처리
#### 함수 인자 권장 작성순서
- 위치 -> 기본 -> 가변 -> 가변 키워드
- 호출 시 인자를 전달하는 과정에서 혼란을 줄일 수 있도록 함
- <span style='color:crimson;'>단, 모든 상황에 적용되는 절대적인 규칙은 아니며, 상황에 따라 유연하게 조정될 수 있음</span>

    ```python
    def func(pos1, pos2, default_arg='default', *args, **kwargs):
        # ...
    ```

##### 인자의 모든 종류를 적용한 예시
```python
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)

func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')

"""
pos1: 1
pos2: 2
default_arg: 3
args: (4, 5, 6)
kwargs: {'key1': 'value1', 'key2': 'value2'}
"""
```
## 재귀함수
- 함수 내부에서 자기 자신을 호출하는 함수
#### 재귀 함수 예시(팩토리얼)
```python
𝑛!
𝑛 ∗ (𝑛−1)!
𝑛 ∗ (𝑛−1) ∗ (𝑛−2)!
…
```
- factorial 함수는 자기 자신을 재귀적으로 호출하여 입력된 숫자 n의 팩토리얼을 계산
- 재귀 호출은 n이 0이 될 때까지 반복되며, 종료 조건을 설정하여 재귀 호출이 멈추도록 함
- 재귀 호출의 결과를 이용하여 문제를 작은 단위의 문제로 분할하고, 분할된 문제들의 결과를 조합하여 최종 결과를 도출
#### 재귀 함수 특징
- 특정 알고리즘 식을 표현할 때 변수의 사용이 줄어들며, 코드의 가독성이 높아짐
- 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성

#### 재귀 함수를 사용하는 이유
- 문제의 자연스러운 표현
  - 복잡한 문제를 간결하고 직관적으로 표현 가능

- 코드 간결성
  - 상황에 따라 반복문보다 알고리즘 코드가 더 간결하고 명확해질 수 있음

- 수학적 문제 해결
  - 수학적 정의가 재귀적으로 표현되는 경우, 직접적인 구현 가능

#### 재귀 함수 활용 시 기억해야 할 것
1. 종료 조건을 명확히
2. 반복되는 호출이 종료 조건을 향하도록

## 내장 함수(built-in function)
- 파이썬이 기본적으로 제공하는 함수(별도의 import 없이 바로 사용 가능)
# 자주 사용되는 내장 함수 예시
numbers = [1, 2, 3, 4, 5]
``` python
print(len(numbers))  # 5
print(max(numbers))  # 5
print(min(numbers))  # 1
print(sum(numbers))  # 15
print(sorted(numbers, reverse=True))  # [5, 4, 3, 2, 1]
```
### 유용한 내장 함수 map & zip
#### `map(function, iterable)`
- 순회 가능한 데이터구조(iterable)의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환
##### `map()` 활용
- SWEA 문제의 input 처럼 문자열 `'1 2 3'`이 입력 되었을 때 활용 예시

```python
numbers1 = input().split()
print(numbers1)  # ['1', '2', '3']

numbers2 = list(map(int, input().split()))
print(numbers2)  # [1, 2, 3]
```
#### `zip(*iterable)`
- 임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

    ```python
    girls = ['jane', 'ashley']
    boys = ['peter', 'jay']
    pair = zip(girls, boys)

    print(pair)  # <zip object at 0x000001C76DE58700>
    print(list(pair))  # [('jane', 'peter'), ('ashley', 'jay')]
    ```

## 함수와 Scope
### Python의 범위(Scope)
- 함수는 코드 내부에 `local scope`를 생성하며, 그 외의 공간인 `global scope`로 구분

### 범위와 변수 관계
- scope
    - global scope : 코드 어디에서든 참조할 수 있는 공간
    - local scope : 함수가 만든 scope (함수 내부에서만 참조 가능)
- variable 
    - global variable : global scope에 정의된 변수
    - local variable : local scope에 정의된 변수

#### 변수 수명주기(lifecycle)
- 변수의 수명주기는 변수가 선언되는 위치와 스코프에 따라 결정됨
1. built-in scope
    - 파이썬이 실행된 이후부터 영원히 유지
2. global scope
    - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
3. local scope
    - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지
#### 이름 검색 규칙(Name Resolution)
- 파이썬에서 사용되는 이름(식별자)들은 특정한 이름공간(namespace)에 저장되어 있음
- 아래와 같은 순서로 이름을 찾아 나가며, LEGB Rule이라고 부름
    1. Local scope : 지역 범위(현재 작업 중인 범위)
    2. Enclosed scope : 지역 범위 한 단계 위 범위
    3. Global scope : 최상단에 위치한 범위
    4. Built-in scope : 모든 것을 담고 있는 범위(정의하지 않고 사용할 수 있는 모든 것)
- <span style='color:crimson;'>함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음</span>

![image](https://github.com/ragu6963/TIL/assets/32388270/15b4f0c6-7f21-4986-8349-fd8740e49573)
#### LEGB Rule
- sum이라는 이름을 global scope에서 사용하게 되면서 <br>기존에 built-in scope에 있던 내장함수 sum을 사용하지 못하게 됨
- sum을 참조 시 LEGB Rule에 따라 global에서 먼저 찾기 때문
- 정수는 못씀
#### `global` 키워드
- 변수의 스코프를 전역 범위로 지정하기 위해 사용
- 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용
#### ‘global’ 키워드 주의사항
- global 키워드 선언 전에 참조 불가
- 매개변수에는 global 키워드 사용 불가