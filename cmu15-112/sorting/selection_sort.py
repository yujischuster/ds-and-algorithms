def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

a = [1, 4]
print(a)
swap(a, 0, 1)
print(a)