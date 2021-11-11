# dict : 순서 없음, {키 : 값}으로 구성
mydic = dict(k1 = 1, k2 = 'mbc', k3 = 3.4)
print(mydic, type(mydic)) # {'k1': 1, 'k2': 'mbc', 'k3': 3.4} <class 'dict'>

dic = {'파이썬':'뱀', '자바':'커피', 'spring':'용수철', 'kbs':9}
print(dic, type(dic), len(dic)) # {'파이썬': '뱀', '자바': '커피', 'spring': '용수철', 'kbs': 9} <class 'dict'> 4
print(dic['자바'])
# print(dic['뱀']) value로 찾을 수 없음 KeyError: '뱀'

dic['오라클'] = '예언자'
print(dic) # {'파이썬': '뱀', '자바': '커피', 'spring': '용수철', 'kbs': 9, '오라클': '예언자'}
del dic['오라클']
print(dic) # {'파이썬': '뱀', '자바': '커피', 'spring': '용수철', 'kbs': 9}
dic.pop('자바')
print(dic) # {'파이썬': '뱀', 'spring': '용수철', 'kbs': 9}
dic['spring'] = '웹용프레임워크'
print(dic) # {'파이썬': '뱀', 'spring': '웹용프레임워크', 'kbs': 9}

print(dic.keys()) # dict_keys(['파이썬', 'spring', 'kbs'])
print(dic.values()) # dict_values(['뱀', '웹용프레임워크', 9])
print(dic.get('파이썬')) # 뱀
print(dic["파이썬"])
print('spring' in dic) # true
print('summer' in dic) # false
