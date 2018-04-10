def stair(n):
    if n == 1 or n == 2:
        return n
    # if n<3: return n
    return stair(n - 1) + stair(n - 2)


num = int(input("how many? >>"))

print(stair(num))
