list=[1,2,5,3]
list1=list.copy()

list.sort()

if(list1==list):
  print("The list is sorted")
else:
  print("The list is unsorted")