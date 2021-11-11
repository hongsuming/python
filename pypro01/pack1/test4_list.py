# list 자료형 : 순서 있음, 변경 가능, 중복 가능
a = [1, 2, 3]
b = [10, a, 20.5, True, '문자열']
print(a) # [1, 2, 3]
print(b) # [10, [1, 2, 3], 20.5, True, '문자열']
print(id(a), id(b)) # 2074450707648 2074450712576

print()
family = ['엄마', '아빠', '나']
family.append('남동생')
family.insert(2, '언니')
family.extend(['할머니', '할아버지']) # 여러 개 추가할 때
family += ['강아지']
family.remove('나')
print(len(family), family) # 7 ['엄마', '아빠', '언니', '남동생', '할머니', '할아버지', '강아지']
print(family.index('남동생')) # 3
print(family[0], family[-1], family[0:6:2]) # 엄마 강아지 ['엄마', '언니', '할머니']

print('중첩 리스트')
aa = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(aa) # [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(aa[0], aa[3], aa[3][1]) # 1 ['a', 'b', 'c'] b

print('복사')
name = ['톰', '제리', '불독']

print(name, id(name)) # ['톰', '제리', '불독'] 2072153242688

name2 = name # 복사
print(name2, id(name2)) # ['톰', '제리', '불독'] 2532626640640

import copy
name3 = copy.deepcopy(name) # 주소가 다름 (별도의 객체를 생성)
print(name3, id(name3)) # ['톰', '제리', '불독'] 2143597732608

name[0] = 'tom'
print(name, id(name)) # ['tom', '제리', '불독'] 2381302071872
print(name2, id(name2)) # ['tom', '제리', '불독'] 2381302071872
print(name3, id(name3)) # 다른 객체이기 때문에 안 바뀜 ['톰', '제리', '불독'] 2381303353984