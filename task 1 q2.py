def pattern(n):
    c=1
    for i in range (1,n+1):
        for j in range (1,i+1):
            print(c, end=" ")
            c=(c%n)+1
        print("\n")
n=int(input("Enter the number of rows:"))
pattern(n)
    