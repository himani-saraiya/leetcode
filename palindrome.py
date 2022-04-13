def pali(a):
    # a=int(input("enter a number   "))
    i=a
    r=0
    while i>0:
        r=r*10+i%10
        i=i//10
    if a==r:
        print("palindrome")
    else:
        print("not")
pali(121)