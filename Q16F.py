n=int(input("Enter a number:"))
for i in range(n):
  for j in range(n-i-1):
    print(" ",end="")
  num=str(11**i)
  for k in range(len(num)):
    print(num[k],end=" ")
  print()