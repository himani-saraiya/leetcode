def list():    
    a=[1,12,3,14,3,8,2,5,5,8]
    i=0
    b=[]
    while i<len(a):
        if a[i] not in b:
            b.append(a[i])
        i=i+1
    b.sort()
    print(b)
list()