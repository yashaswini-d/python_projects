from collections import defaultdict

d={'a':20, 'b':21, 'c':22, 'd':23}
for k,v in d.items():
    print(k,v)

d = defaultdict(list)
for x in range(4):
    d[x] = x*2
print(d.items()