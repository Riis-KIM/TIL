## 알고리즘
유한한 단계를 통해 **문제를 해결하기 위한 절차나 방법**이다. 주로 컴퓨터 용어로 쓰이며, 컴퓨터가 어떤 일을 수행하기 위한 단계적 방법을 말한다.

#### 알고리즘 표현 방법
1. 의사코드(pseudocode)
2. 순서도

### 좋은 알고리즘이란?
1. 정확성 : 얼마나 정확하게 동작하는가
2. 작업량 : 얼마나 적은 연산으로 원하는 결과를 얻어내는가
3. 메모리 사용량 : 얼마나 적은 메모리를 사용하는가
4. 단순성 : 얼마나 단순한가
5. 최적성 : 더 이상 개선할 여지없이 최적화되었는가
  
### 알고리즘 선택 방법
문제를 해결할 때 다양한 알고리즘 선택 가능
- 성능 분석 필요
  - 많은 문제에서 성능 분석을 기준으로 알고리즘 작업량을 비교
- 시간 복잡도(Time Complexity)
  - 실제 걸리는 시간을 측정
  - 실행되는 명령문의 개수를 계산
시간 복잡도 -> 빅 오(O) 표기법
시간 복잡도 함수 중에서 가장 큰 영향력을 주는 n에 대한 항을 표시
계수는 생략하여 표시
O(3n+2) = O(3n) = O(n)
ex) n개의 데이터를 입력 받아 저장한 후 각 데이터에 1씩 증가시킨 후 각 데이터를 화면에 출력하는 알고리즘의 시간복잡도는? -->O(n)

### 배열
- 일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조
- 프로그램 내에서 여러 개의 변수가 필요할 때, 일일이 다른 변수명을 이용해 자료에 접근하는 것은 매우 비효율적
- 배열을 사용하면 하나의 선언을 통해 둘 이상의 변수를 선언 가능
- 단순히 다수의 변수 선언을 의미하는 것이 아니라, 다수의 변수로는 하기 힘든 작업을 배열을 활용해 쉽게 가능

#### 1차원 배열의 선언
- 별도의 선언 방법이 없으면 변수에 처음 값을 할당할 때 생성
- 예시/ ARR=list(), Arr=[], Arr=[1,2,3] Arr=[0]*10
- Arr[0] = 10 # 배열 ARR의 0번 원소에 10을 저장하라
- Arr[idx] = 20 #배열 ARR의 idx번 원소에 20을 저장하라\

### 정렬
- 2개 이상의 자료를 특정 기준에 의해 작은 값부터 큰 값(오름차순), 혹은 그 반대(내림차순)로 재배열하는것
  - 버블 정렬
  - 카운팅 정렬
  - 선택 정렬
  - 퀵 정렬
  - 삽입 정렬
  - 병합 정렬

#### 버블 정렬
- 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식
- 정렬 과정
  - 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동
  - 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬된다
  - 교환하여 자리를 이동하는 모습이 물 위를 올라오는 거품과 비슷해 버블정렬
- 시간 복잡도 = O(n**2)

#### 카운팅 정렬
- 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적 알고리즘
- 제약사항
  - 정수나 정수로 표현할 수 있는 자료에 대해서만 적용가능  : 각 항목의 발생 회수를 기록하기 위해, 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문이다.
  - 카운트들을 위한 충분한 공간을 할당하려면 집합 내 가장 큰 정수를 알아야 함.
- 시간 복잡도 = O(n+k), n은 리스트 길이, k는 정수의 최대값
- 위치 정보를 가지고 있을 경우 앞에서부터 정렬 시 문제가 생길 수 있음

#### 완전 검색
- 완전 검색 방법은 문제의 해법으로 생각할 수 있는 모든 경우의 수를 나열해 확인하는 기법이다.
- Brute-force 혹은 generate-and-test 기법이라고도 불린다
- 모든 경우의 수를 테스트한 후, 최종 해법을 도출한다.
- 일반적으로 경우의 수가 상대적으로 작을 때 유용하다
- 모든 경우의 수를 생성하고 테스트하기 때문에 수행 속도는 느리지만, 해답을 찾아내지 못할 확률이 작다

#### 순열

#### 탐욕(그리디) 알고리즘
- 탐욕 알고리즘은 최적해를 구하는 데 사용되는 근시안적 방법
- 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행하여 최종적인 해답에 도달
- 각 선택의 시점에서 이루어지는 결정은 지역적으로는 최고지만, 그 선택들을 계속 수집하여 최종적인 해답을 만들었다고 하며, 최적이라는 보장은 없다.
- 일반적으로, 머릿속에 떠오르는 생각을 검증 없이 바로 구현하면 Greedy 접근이 된다.
- 1. 해 선택
- 2. 실행 가능성 검사
- 3. 해 검사