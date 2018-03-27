a, b, c = map(int, input().split())

result = 0

if a > b:
    if a > c:
        if b > c:
            result = b
        else:
            result = c
    else:
        result = a
else:
    if a < c:
        if b < c:
            result = b
        else:
            result = c
    else:
        result = a

print(result)

######

a = list(input("input three integer values > ").split())
a.sort()
print(a[1])

######

a = list(input("input three integer values > ").split())
a.remove(min(a))
print(min(a))

######

# a, b, c = map(int, input("input three integer values > ").split())
a = list(input("input three integer values > ").split())
