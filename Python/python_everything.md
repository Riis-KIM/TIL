## 아스키코드

문자 -> 아스키코드 : ord()
아스키코드 -> 문자 : chr()
```python
print(chr(45))
print(ord("A"))
```

## 별찍기

```python
for i in range(B): # 밑보다 스페이스바 1개 더 많음
    print(' '*(B-i+1)+'*'*(i+1))
for i in range(1,B+1):
    print(" "*(B-i) + "*"*i)    
```
## 딕셔너리 조작
- setdefault: 키-값 쌍 추가
  - x.setdefault('key',value)
- update: 키의 값 수정, 키가 없으면 키-값 쌍 추가
  - x.update(a=90)
  - update({1:'one',2:'two'})
- pop, del : 키-값 쌍 삭제하기
  - x.pop('a')
  - del x['a']
- popitem : 맨 마지막 키-값 쌍 삭제하기
  - x.popitem()
- clear : 모든 키-값 쌍 삭제하기
  - x.clear()
- get : 키의 값 가져오기
  - x.get('a')
- item, keys, values : 키-값 쌍 모두 가져오는 메서드
  - x.items()
  - x.keys()
  - x.values()

## 출력 메세지 추가 설정

 `\033[{Code number}m` + {Output text} + `\033[0m`
 
