def list(a,target):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if target-a[i]==a[j]:
                return [i,j]
print(list([1,2,6,4,7],6))
