def dfs_stack(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            print(node.v)
            stack.append(node.r)
            stack.append(node.l) 

def build_prefix(a):
    p = [0]*(len(a)+1)
    for i in range(len(a)):
        p[i+1] = p[i] + a[i]
    return p

def query(p, l, r):
    return p[r+1] - p[l]