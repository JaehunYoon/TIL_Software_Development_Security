# skip을 포함하는 문자열인 경우 rejected를 출력하고
# 구분선을 출력하지 않는 함수
def skip(string):
    if string.find("skip") == -1:  # find 대신 in 써도 됨
        return string
    else:
        return "rejected"

string = ""

# quit을 입력할 때까지 반복하여 사용자 입력을 받음
while string != "quit":
    string = input("please input string >> ")
    
    print(skip(string))
    print("-" * 10)
