# 묶음형 자료형 : str - 순서를 갖음, 수정 불가 (슬라이싱 가능)
s = 'sequence'
print(s)
print(len(s), s.count('e'), s.find('e'), s.find('e', 3), s.rfind('e')) # 8 3 1 4 7
print(s.startswith('s'), s.startswith('a')) # 's'로 시작하는지 / 'a'로 시작하는지 True False

print('수정 불가')
ss = "mbc"
print(ss, id(ss))
ss = "abc"
print(ss, id(ss))

print('슬라이싱')
print(s[0], s[2:4], s[:3], s[:3]) # s qu seq seq
print(s[-1], s[-4:-1], s[-4:]) # e enc ence
print(s[1:7:2]) # :2 증가치 의미 (생략하면 1) eun
print(id(s))
# s[0] = 'k' 수정 불가이기 때문에 에러 TypeError: 'str' object does not support item assignment

print('문자열 짜르기 & 붙이기')
s2 = 'kbs mbc'
print(s2) # kbs mbc
s3 = s2.split(sep = ' ') 
print(s3) # ['kbs', 'mbc']
s4 = ','.join(s3)
print(s4) # kbs,mbc
s5 = s4.replace('kbs', 'jtbc')
print(s5) # jtbc,mbc