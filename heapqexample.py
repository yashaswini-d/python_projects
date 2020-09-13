import heapq
a = [66, 1, 87, 71, 97]
heapq.heapify(a)
print(a)
a.append(12)
print(a)
heapq.heapify(a)
print(a)
heapq.heappush(a,27)
print(a)
print("pushing 17")
heapq.heappush(a,16)
print(a)

print(heapq.heapreplace(a,3))
print(a)
print(heapq.heappushpop(a,28))
print(a)



