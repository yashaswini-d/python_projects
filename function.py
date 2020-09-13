def add(* args):
    sum=0
    for i in args:
        sum += i
    return sum
print(add(10,20,30))
print(add(10,20,30,40,50))
