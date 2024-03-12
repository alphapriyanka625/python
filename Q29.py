n=int(input("Enter a number:"))
table=list(map(lambda x:f'10*{x}={10*x}',range(1,n+1)))

print(table)