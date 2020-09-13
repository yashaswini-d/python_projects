from collections import Counter
a=[1,2,3,4,5,6,7,8,9,1,1,13,2,5,6,7,8,5,9]
a=Counter(a)
print(a.most_common(5))

num=[1,2,3,4,5,6,7,8,9]
squares=[x**2 for x in num]
cube=[x**3 for x in num]
print(squares)
print(cube)


