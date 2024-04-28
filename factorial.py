n=int(input("enter the value of n:"))
factorial=1
if n<1:
  print("factorial no exist")
elif(n==0):
  print("the factorial is 1")
else:
  for i in range(1,n+1):
    factorial=factorial*i
print("factorial=",factorial)