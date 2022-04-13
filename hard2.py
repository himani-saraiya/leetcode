def marg(a):
    l=[]
    for i in a:
        for j in i:
            l.append(j)
    l.sort()
    return l
print(marg([[1,4,5],[1,3,4],[2,6]]))