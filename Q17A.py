n=int(input("enter the number : "))
temp=n
rev=0
while(n>0):
   dig=n%10
   rev=rev*10+dig
   n=n//10
if(temp==rev):
  print("the no is palindrome")
else:
  print("its not a palindrome")