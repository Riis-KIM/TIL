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
