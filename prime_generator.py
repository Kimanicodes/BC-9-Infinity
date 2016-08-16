# solution 1 (using two nested for loops)
def primeGenerator(k):
    myList=[]
    if k<2:
        return myList
    for n in range(2, k+1):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            myList.append(n)

    return myList
