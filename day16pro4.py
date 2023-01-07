def reverse1(n):
    return (i[::-1] for i in n)
a = input().strip().split()
print(*reverse1(a))
