# function that no return value

def func1(*a):  # *a = 가변인자
    print(a * 3)


print("Start")
func1('y', 's', 'w')

# function that return value

def sum(a, b):
    return a+b

a,b = map(int, input().split())
res = sum(a, b)
print(res)

# 함수는 선언하고 호출하는 위치가 중요하다.
# C언어처럼 앞에서 프로토타입을 선언할 수 없을까?
# -> 아마 안될 것.
