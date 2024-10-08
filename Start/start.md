### SW 문제 해결 역량
- 프로그램을 하기 위한 많은 제약 조건과 요구사항을 이해하고 최선의 방법을 찾아내는 능력
- 프로그래머가 사용하는 언어나 라이브러리, 자료구조, 알고리즘에 대한 지식을 적재적소에 퍼즐을 배치하듯 이들을 연결하여 큰 그림을 만드는 능력이라 할 수 있다.
- 문제 해결 역량은 추상적인 기술이다.
  - 프로그래밍 언어, 알고리즘처럼 명확히 정의된 실체가 없다.
  - 무작정 알고리즘을 암기하고 문제를 풀어본다고 향상되지 않는다.
- 훈련이 필요하다

#### 문제 해결 과정
1. 문제를 읽고 이해한다.
2. 문제를 익숙한 용어로 재정의한다.
3. 어떻게 해결할지 계획을 세운다.
   1. 손 코딩
4. 계획을 검증한다.
   1. 반례찾기와 복잡도 계산과 같이 논리적인 하점을 찾는다
5. 프로그램으로 구현한다.
   1. 디버깅
6. 어떻게 풀었는지 돌아보고, 개선할 방법이 있는지 찾아본다.
- 한번 틀렸을 때 못돌아오는 경우, 설계가 안되는 경우, 설계는 되거나 구현이 안되는 경우

#### 알고리즘 효율
- 공간적 효율성과 시간적 효율성
  - 공간적 효율성은 연산량 대비 얼마나 적은 메모리 공간을 요하는 가를 말한다.
  - 시간적 효율성은 연산량 대비 얼마나 적은 시간을 요하는 가를 말한다.
  - 효율성을 뒤집어 표현하면 복잡도가 된다. 복잡도가 높을수록 효율성 떨어짐
#### 복잡도의 점근적 표기
- 시간복잡도는 입력 크기에 대한 함수로 표기하는데, 이 함수는 주로 여러개의 항을 가지는 다항식이다.
- 이를 단순한 함수로 표현하기 위해 점근적 표기를 사용한다.
- 입력 크기 n이 무한히 커질 때의 복잡도를 간단히 표현하기 위해 사용
- O 표기 <-- 최대 시간
- 빅 오메가 표기 <-- 최소 시간
- 빅 세타 표기 <-- 평균 시간
- 빅 오 표기
  - 복잡도의 점근적 상한을 나타낸다
  - 복잡도 f(n) = 2n**2-7n+4라면 O(n2)이다.

#### 비트연산
- 1 bit : 0과 1을 표현하는 정보의 단위
- 1 byte : 8 bit를 묶어 1byte라고 한다
- 컴퓨터의 CPU는 0과 1로 다루어 동작되며, 내부적으로 비트 연산을 사용하여 덧셈, 뺄셈, 곱셈 등을 계산한다.   
- a AND b: a, b 둘다 1일때만 결과가 1
- a OR b: a, b 둘중 하나만 1이여도 결과 1
- a XOR b: a, b 둘 다 1일 경우는 0이 나온다.(같으면 0, 다르면 1)
- 비트 연산자
  - left shift <<:특정 수의 비트를 왼쪽으로 밀어낸다
  - right shift >>:특정 수의 비트를 오른쪽으로 밀어낸다(우측 비트들이 제거된다)
- 1 << n : 2**n의 값을 가진다
- 임베디드 분야에서 계산을 빠르게 하기 위해 사용된다
- i & (1<<n)
  - i의 n번째 비트가 1인지 아닌지를 확인하는 것
#### 음수 표현 방법
- 컴퓨터는 음수를 2의 보수로 관리한다
- 맨 앞자리 bit(MSB)는 음수 or 양수를 구분하는 비트이다
#### not 연산자
- ~not : 모든 비트를 반전시킨다.
- 8비트일때 ~(0001 1111) -> 1110 0000
#### 실수
- 파이썬은 다른 언어와 달리 내부적으로 더 큰 규모의 자료구조를 사용해 훨씬 넓은 범위의 실수 표현 가능
- 실수는 정확한 값이 아니라 근사값으로 저장되는데 이때 생기는 작은 오차가 계산 과정에서 다른 결과를 가져옴
- 컴퓨터는 실수를 표현하기 위해 부동 소수점(floating-point) 표기법 사용
- 이 표기법을 IEEE 754이라는 컴퓨터에서 부동소수점을 표기하는 국제 표준
- 부동 소수점 표기 방법은 소수점의 위치를 고정시켜 표현하는 방식
  - 소수점으 ㅣ위치를 왼쪽의 가장 유요한 숫자 다음으로 고정시키고 밑수의 지수승으로 표현
  - 32비트 구조
  - 부호 1피트 : 0이면 양, 1이면 음
  - 지수부 8 비트 : 부동소수점의 크기 + bias값
  - 가수부 23 비트 : 실질적 수
- 