"""
def hanoi(n):
    if n > 1:
        return hanoi(n - 1) + 1 + hanoi(n - 1)  # 유한성 조건
    else:
        return 1


num = int(input("please input hanoi number >> "))  # 입력 (0개 이상)
print(hanoi(num))  # 출력 (1개 이상)
"""

n = int(input("input hanoi column's number >> "))
print(2**n-1)
# 문제 분해를 통해 구조를 알아낸 후 이를 수학적으로 구현한다.
