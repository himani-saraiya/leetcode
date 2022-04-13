def num(a):
    b=int(input("enter number"))
    for i in range(len(a)):
        if a[i]==b:
            return i
        else:
            pass
print(num([1,2,3,4,5]))            