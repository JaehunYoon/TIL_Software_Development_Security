def knudsen():  # 크누센의 실험식을 이용한 염분 계산
    clear()  # 화면 초기화
    print("<크누센의 실험식>")
    print()
    print("염소 이온의 양을 입력해주세요.")

    while True:  # 염분 값이 정상적으로 출력될 때까지 반복
        try:
            Cl = float(input("Cl >> "))  # Cl(염소 이온) 값 입력
            if check_positive(Cl):  # Cl이 양수일 경우 조건문 수행
                salt = 0.030 + (1.805 * Cl)  # 크누센의 실험식에 Cl 대입 후 연산
                if check_permillage(salt):  # 염분이 천분율 범위에 속할 경우 조건문 수행 (0 <= salt <= 1,000)
                    print("염소 이온이 {}일 때, 염분 값은 {}‰ 입니다.".format(Cl, salt))  # 결과 출력
                    return  # 출력 수행 후 프로그램 종료
        except:  # 오류 예외 처리
            print("잘못된 값입니다.")


def regular():  # 표준화된 염분 계산식을 이용한 염분 계산
    clear()  # 화면 초기화
    print("<기본 공식>")
    print()
    print("염류와 해수의 양을 입력해주세요. (단위 : g)")

    while True:  # 염분 값이 정상적으로 출력될 때까지 반복
        try:
            SA, sea = map(float, input("염류, 해수 >> ").split())  # 염류, 해수 값 입력

            if check_positive(SA) and check_positive(sea):  # SA(염류)와 sea(해수)가 모두 양수일 경우 조건문 실행
                salt = (SA / sea) * 1000  # 염분 계산식에 SA, sea 대입 후 연산
                if check_permillage(salt):  # 염분이 천분율 범위에 속할 경우 조건문 수행 (0 <= salt <= 1,000)
                    print("염류가 {}g, 해수가 {}g 일때, 염분 값은 {}‰ 입니다.".format(SA, sea, salt))  # 결과 출력
                    return  # 출력 수행 후 프로그램 종료
        except:  # 예외 처리
            clear()  # 화면 초기화
            if sea == 0:  # 분모가 0이 될 수 없으므로 예외 처리
                print("해수의 양은 0보다 커야 합니다.")
            else:
                print("잘못된 값입니다.")
    

def check_permillage(salt):  # 염분이 천분율 범위에 속하는 지 판별해주는 함수
    if 0 <= salt <= 1000:  # 염분이 0 이상 1,000 이하일 경우 True 반환
        return True
    else:
        print("염분은 0‰ 보다 작거나 1,000‰ 보다 클 수 없습니다.")

def check_positive(value):  # 인자 값이 양수인지 판별해주는 함수
    if value >= 0:  # 인자 값이 0 이상일 경우 True 반환
        return True
    else:
        print("음수는 입력할 수 없습니다.")


def clear():  # 화면 초기화 함수
    print("\n" * 100)  # 개행 100번


print("이 프로그램은 무료로 염분을 구해드립니다!!")
print("1. 크누센의 실험식 (염소 이온 입력)")
print("2. 일반 공식 (염류, 해수의 양 입력)")
print()
print("* 염분은 해수 1kg를 기준으로 계산합니다.")
print()
print("염분을 구할 때 사용할 방법을 선택해주세요! ")

while True:  # 정상적으로 select를 입력받고 함수가 실행될 때까지 반복
    print("----------------------------------------")
    try:
        select = int(input(">> "))  # 염분 계산 방법 입력
        if select == 1:  # 1 입력 시 크누센의 실험식 이용
            knudsen()
            break  # knudsen 함수 실행 후 프로그램이 종료될 수 있도록 반복문 탈출
        elif select == 2:  # 2 입력 시 기존 염분 계산식 이용
            regular()
            break  # regular 함수 실행 후 프로그램이 종료될 수 있도록 반복문 탈출
        else:  # 1 또는 2를 제외한 다른 정수를 입력했을 경우 예외 처리
            clear()
            print("잘못된 값입니다.")
    except:  # 예외 처리
        clear()
        print("잘못된 값입니다.")
