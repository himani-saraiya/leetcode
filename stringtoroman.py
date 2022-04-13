values=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
symbol=["M","CM","D","CD","D","XD","L","XL","X","IX","V","IV","I"]
num=int(input("enter a integer number:"))
roman=""
for i in range(len(values)):
    m=num//values[i]
    num=num%values[i]
    for j in range(m):
        roman+=symbol[i]
    num=num%values[i]
print(roman)