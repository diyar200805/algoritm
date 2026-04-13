#ВОПРОС № 1 № 2
def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n-1) + fib_rec(n-2)

def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a  

class Node:
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None

def dfs(root):
    if root:
        print(root.v)
        dfs(root.l)
        dfs(root.r)
