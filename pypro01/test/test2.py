li = [3, 5, 7, 9]

for i in li:
    for j in range(1, 10):
        print('{} * {} = {}' .format(i, j, i*j), end=' ')
    print()
    
print()
li = [1,2,2,3,2,1]
s = set(li)
li = list(s)
print(li)

print()
sum = 0
for i in range(1, 101):
    if i %3 == 0:
        sum += i
print(sum)