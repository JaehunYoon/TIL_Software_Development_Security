# c = input("please input cryptogram (10 characters) >> ").split()
#
# cryptogram = {c[0]: 1, c[1]: 2, c[2]: 3, c[3]: 4, c[4]: 5, c[5]: 6, c[6]: 7, c[7]: 8, c[8]: 9, c[9]: 10, ' ': ' '}
#
# print(cryptogram)

code_table = input("input code table (10 characters) >> ")
cryptogram = input("input cryptogram >> ")

# i = 0
# while i < len(b):
#     if b[i] != ' ':
#         print(a.find(b[i]), end="")
#     else:
#         print(b[i], end="")
#     i = i + 1

# i = 0
# while i < len(b):
#     print(a.find(b[i]) if b[i] != ' ' else b[i], end='')
#     i = i + 1

for i in cryptogram:
    print(code_table.find(i) if i != ' ' else i, end='')
