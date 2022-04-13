def fun():
    a=[1,4,3]
    b=[2,5,6]
    i=0
    while i<len(b):
        a.append(b[i])
        i=i+1
    a.sort()
    print(a)
fun()       
