def knudsen():
    print("test Knudsen Salt")


def regular():
    print("test regular salt")


print("Salt Salt Salt Salt")
print()
print("염분을 구해주는 파이썬 코드입니다.")
print("어떤 방법으로 염분을 구하시겠습니까?")
print()
print("1. 염분비 일정의 법칙 (크누센의 실험식)")
print("2. 일반 염분 공식")

while True:
    print()
    select = int(input("음, 저는.. >> "))

    if select == 1:
        print("염분비 일정의 법칙으로 염분을 구해봅시다!")
        knudsen()
    elif select == 2:
        print("일반 염분 공식으로 염분을 구해봅시다!")
        regular()
    else:
        print("숫자를 잘못 입력하셨습니다..")

