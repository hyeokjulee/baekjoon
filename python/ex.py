A = [[0 for col in range(3)] for row in range(3)]
for i in range(3):
    for j in range(3):
        A[i][j] = i + j

print(A[1].index(3))