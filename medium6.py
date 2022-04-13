def list(a,target):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if target-a[i]==a[j]:
                return [[a[i],a[j]],[target]]
print(list([1,2,6,4,7],7))

