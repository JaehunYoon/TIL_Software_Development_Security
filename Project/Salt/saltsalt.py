def knudsen():
    clear()
    print("<크누센의 실험식>")
    print()
    print("염소 이온의 양을 입력해주세요.")

    while True:    
        try:
            Cl = float(input("Cl >> "))
            if check_positive(Cl):
                salt = 0.030 + (1.805 * Cl)
                if check_permillage(salt):
                    print("염소 이온이 {}일 때, 염분 값은 {}‰ 입니다.".format(Cl, salt))
                    return
        except:
            print("잘못된 값입니다.")


def regular():
    clear()
    print("<기본 공식>")
    print()
    print("염류와 해수의 양을 입력해주세요. (단위 : g)")

    while True:
        try:
            SA, sea = map(float, input("염류, 해수 >> ").split())

            if check_positive(SA) and check_positive(sea):
                salt = (SA / sea) * 1000
                if check_permillage(salt):
                    print("염류가 {}g, 해수가 {}g 일때, 염분 값은 {}‰ 입니다.".format(SA, sea, salt))
                    return
        except:
            clear()
            if sea == 0:
                print("해수의 양은 0보다 커야 합니다.")
            else:
                print("잘못된 값입니다.")
    

def check_permillage(salt):
    if 0 <= salt <= 1000:
        return True
    else:
        print("염분은 0‰ 보다 작거나 1,000‰ 보다 클 수 없습니다.")

def check_positive(value):
    if value >= 0:
        return True
    else:
        print("음수는 입력할 수 없습니다.")


def clear():
    print("\n" * 100)


print("이 프로그램은 무료로 염분을 구해드립니다!!")
print("1. 크누센의 실험식 (염소 이온 입력)")
print("2. 일반 공식 (염류, 해수의 양 입력)")
print()
print("* 염분은 해수 1kg를 기준으로 계산합니다.")
print()
print("염분을 구할 때 사용할 방법을 선택해주세요! ")

while True:
    print("----------------------------------------")
    try:
        select = int(input(">> "))
        if select == 1:
            knudsen()
            break
        elif select == 2:
            regular()
            break
        else:
            clear()
            print("잘못된 값입니다.")
    except:
        clear()
        print("잘못된 값입니다.")