# -*- coding:utf-8 -*-
# 한글 적용

"""
age = input("Input your age > ")

if int(age) >= 20:  # 괄호를 써도 되고 안써도 됨
    print("Party tonight")
# 파이썬의 코드 구분은 "들여쓰기" 로 수행된다.
# 함수, 조건, 반복 구조 등 내포가 필요한 구문은
# 콜론(:)으로 구분한다.
else:
    print("Study tonight")
"""

age = input("나이를 입력하세요 > ")
if int(age) >= 20:
    print("Party tonight")
else:
    print("Study tonight")

# 삼항연산자
# format : 명령문 if 조건 else 거짓일 때의 명령문

age = input("나이를 입력하세요 > ")

print("Party tonight" if int(age) >= 20 else "Study tonight")  # 삼항연산자
