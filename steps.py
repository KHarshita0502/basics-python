x=int(input("enter the no of steps"))
if(x<5):
    print("1")
elif(x%5==0):
    print(x/5)
else:
    x//5+1
    print("3")