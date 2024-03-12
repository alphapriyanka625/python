rows =int(input("enter number of rows : "))
for i in range(0,rows+1):
    num = i
    for j in range(0, i):
        print(num, end=' ')
    print("\r")
