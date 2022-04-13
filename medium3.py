def skip():
    a=[1,2,3,4,5,6,7,8,9]
    b=int(input("number  "))
    i=0
    l=[]
    while i<len(a):
        if a[i]==b:
            pass
        else:
            l.append(a[i])
            # print(a[i])
        i=i+1
    print(l)
skip()