#ВОПРОС № 3 № 4 
def nested(n):
    count = 0
    for i in range(n):
        for j in range(i):
            count += 1
    return count 

def multiply(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]
    return C 

def nested(n):
    count = 0
    for i in range(n):
        for j in range(i):
            count += 1
    return count
