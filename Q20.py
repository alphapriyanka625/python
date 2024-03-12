list=[]
n=int(input("how many number you want to enter in list:"))

for i in range(1,n+1):
  t=int(input(f"enter number {i}:"))
  list.append(t)

print(list)

list.sort()
print("maximum element:",list[n-1])
print("minimum element:",list[0])