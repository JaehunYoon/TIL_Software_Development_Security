# 가상의 이메일 전송 함수

def send_mail(from_mail, to_mail, subject, contents):
    print("from \t" + from_mail)
    print("To : \t" + to_mail)
    print("Subject : \t" + subject)
    print("*" * 20)
    print(contents)
    print("*" * 20)
    print("*" * 20)

teacher_email = "skyjjw79@hanmail.net"
my_email = "h4lo@h4lo.kr"

users = []
users.append({'name': 'Boo', 'email': 'goodasd123@naver.com'})
users.append({'name': 'John', 'email': 'goodasd123@gmail.com'})

'''
                user0                   user1
        --------------------------------------------
name             Boo                    John
email   goodasd123@naver.com    goodasd123@gmail.com
'''

contents = '''This is DSM
my leader is Bo yeong Bo yeong
I love you
'''

for user in users:
    title = 'Dear. ' + user['name']
    send_mail(my_email, user['email'], title, contents)
