a = int(input())
b = int(input())
c = int(input())def lone_sum(a, b, c):
    if a == b or a == c or b == c:
        return 0
    elif a >= b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return a+b+c
print(lone_sum(a, b, c))

