# tuple : list와 유사하나 읽기 전용 - 속도가 빠름
# t = (1, 2, 3, 4, 3)
t = 1, 2, 3, 4, 3
print(t, type(t), len(t)) # (1, 2, 3, 4, 3) <class 'tuple'> 5
print(t.count(3), t.index(4)) # 2 3
print(t[0], t[0:3]) # 1 (1, 2, 3)
# t[0] = 10 변경 불가 TypeError: 'tuple' object does not support item assignment

imsi = list(t) # 형 변환
print(imsi, type(imsi)) # [1, 2, 3, 4, 3] <class 'list'>
imsi[0] = 10
t = tuple(imsi) # 형 변환
print(t, type(t)) # (10, 2, 3, 4, 3) <class 'tuple'>

aa = (1)
print(aa, type(aa)) # 1 <class 'int'>
bb = (1,)
print(bb, type(bb)) # (1,) <class 'tuple'>