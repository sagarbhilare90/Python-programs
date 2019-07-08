num=100
a=0
b=1
if num==1:
    print("1")
for i in range(num):
    c=a+b
    a,b=b,c
    if c<=100:
        print(c)
    else:
        break