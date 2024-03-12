A=[
  [1,2,3], #x[0]=>x[0][0],X[0][1]
  [2,3,4],
  [3,4,5]
]

B=[
  [1,2,3],
  [2,3,4],
  [3,4,5]
]

result=[
  [0,0,0],
  [0,0,0],
  [0,0,0]
]

for i in range(len(A)):
  for j in range(len(A[0])):
    result[i][j]=A[i][j]+B[i][j]

for i in result:
  print(i)

