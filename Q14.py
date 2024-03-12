num=int(input("Enter a number : "))
temp=num

sum=0
while temp>0:
  dig=temp%10
  sum=dig**3+sum
  temp=temp//10

if(num==sum):
   print(num,"is a armstrong number")
else:
  print(num,"is a not armstrong number")