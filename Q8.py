num1=int(input("Enter a number : "))
fac=1
if(num1<0):
  print("Factorial does not exist")
elif(num1==0):
  print("Factorial of 0 is 1")
else:
  for i in range(1,num1+1):
    fac=fac*i
  print("Factorial is : ",fac)