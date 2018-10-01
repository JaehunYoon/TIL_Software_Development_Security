while True:
    a = input("ㄱㄱ > ")
    try:
        if int(a) == 1:
            print("The end")
            break
        else:
            print("This is not one..")
    except Exception as e:
        print("This is not one..")

# while True:
#     a = input("고고 > ")
#     if a == '1' and int(a) == 1:
#         print("The end")
#         break
#     else:
#         print("this is not one")
