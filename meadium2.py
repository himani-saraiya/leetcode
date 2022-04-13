from audioop import reverse

def fun(a):
    # a=int(input("enter number"))
    i=0
    while a<0:
        r=-1
        a=a*-1
    while a>0:
        i=i*10+a%10
        a=a//10
    print(i,"reverse")
fun(234)
