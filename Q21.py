input_list=list(map(str,input("enter a comma separated list of numbers:").split(",")))
unique_list=[]

for item in input_list:
  if item not in unique_list:
    unique_list.append(item)

input_list=unique_list
print("list after the removing duplicate:",input_list)