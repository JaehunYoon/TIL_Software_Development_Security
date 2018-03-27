# <코드축약>

# 키보드를 사용하여 두 정수를 입력하면 덧셈, 뺄셈, 곱셈, 나눗셈, 몫, 나머지가 출력되는 계산기 프로그램을 작성하시오.

# Code 1
# a = input()
# b = input()
# a = int(a)
# b = int(b)
# print(a+b)
# print(a-b)
# print(a*b)
# print("%.2f" %(a/b))
# print(int(a/b))
# print(a%b)

# Code 2
# a, b = input("input two integer value > ").split()
#
# a = int(a)
# b = int(b)
#
# print(a + b)
# print(a - b)
# print(a * b)
# print("%.2f" % (a / b))
# print(a // b)
# print(a % b)

# Code 3
# a, b = map(int, input("input two integer value > ").split())
#
# print(a + b)
# print(a - b)
# print(a * b)
# print("%.2f" % (a / b))
# print(a // b)
# print(a % b)

# Code 4
a, b = map(int, input("input two integer value > ").split())
print(a + b, a - b, a * b, "%.2f" % (a / b), a // b, a % b, sep='\n')


