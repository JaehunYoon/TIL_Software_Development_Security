# for i in range(1, 10):
#     for j in range(1, 10):
#         print("{} x {} = {} ".format(i, j, i * j), end=' ')
#         if j % 3 == 0:
#             print('\n')
#     print('\n')

# list_a = [3, 6, 9, 12]
# res1 = []
# for n in list_a:
#     res1.append(n-1)
# print(res1)
#
# res2 = [n-2 for n in list_a]
# print(res2)

print([[i * j for i in range(1, 10)] for j in range(1, 10)])
