def fib(val):
    a=0
    b=1
    fib_series=[]
    ##fib_series.append(1)
    while b <= val:
        fib_series.append(b)
        temp=a
        a=b
        b=temp+b
    return fib_series
print(fib(100))



