def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

def binary_search(a, x):
    l, r = 0, len(a)-1
    while l <= r:
        m = (l+r)//2
        if a[m] == x:
            return m
        elif a[m] < x:
            l = m+1
        else:
            r = m-1
    return -1  

def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a