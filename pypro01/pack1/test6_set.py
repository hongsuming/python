# set : 순서 없음,  중복 안 됨
a = {1, 2, 3, 1}
print(a, type(a), len(a)) # {1, 2, 3} <class 'set'> 3
# print(a[0]) 슬라이싱 불가 TypeError: 'set' object is not subscriptable

b = {3, 4, 5}
# print(a + b) TypeError: unsupported operand type(s) for +: 'set' and 'set'
print(a.union(b)) # 합집합 {1, 2, 3, 4, 5}
print(a.intersection(b)) # 교집합 {3}
print(a | b, a - b, a & b) # 합집합 차집합 교집합 {1, 2, 3, 4, 5} {1, 2} {3}

a.update({6, 7})
print(a) # {1, 2, 3, 6, 7}
a.remove(6)
print(a) # {1, 2, 3, 7}

li = [1, 2, 2, 3, 2, 1]
print(li) # [1, 2, 2, 3, 2, 1]
s = set(li) # 중복이 안 되는 set으로 형 변환하고
li = list(s) # 다시 list로 형 변환
print(li) # [1, 2, 3]