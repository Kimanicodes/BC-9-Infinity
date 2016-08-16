#solution 1
def fib1(n):
    l=[0,1]
    i=1
    num = l[i]
    while True:
        if num>=n:
            return l
        else:
            l.append(l[i]+l[i-1])
            i+=1
            num=l[i]
#solution 2
def fib(n): 
    myList=[]
    a, b = 0, 1
    while a < n:
        myList.append(a)
        a, b = b, a+b
    return myList
    
print(fib1(20))
print(fib(19))