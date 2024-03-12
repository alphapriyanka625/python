A=[
  [1,5,7],
  [4,0,2],
  [6,0,3]]
B=[
  [1,0],
  [4,0],
  [5,0]]

#3x3  3x2-->3x2

c=[
  [0,0],
  [0,0],
  [0,0]]

for i in range(0,len(c)):
  for j in range(0,len(c[0])):
    for k in range(0,len(B)):
       c[i][j]+=A[i][k]*B[k][j]

for row in c:
  print(row)