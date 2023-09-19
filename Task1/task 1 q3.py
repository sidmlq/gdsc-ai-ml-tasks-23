def mult(n, mat1, mat2):
    result = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += mat1[i][k] * mat2[k][j]

    trace = sum(result[i][i] for i in range(n))
    return trace

n = int(input())
mat1 = []
mat2 = []

for _ in range(n):
    row = list(map(int, input().split()))
    mat1.append(row)

for _ in range(n):
    row = list(map(int, input().split()))
    mat2.append(row)

trace = mult(n, mat1, mat2)
print("Trace of the product matrix is:", trace)
