from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep
import smtplib

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465

SMTP_USER = input("Gmail ID : ")
SMTP_PASSWORD = input("Gmail PW : ")

print("\n" * 100)

def send_mail(name, addr):
    try:
        msg = MIMEMultipart()

        msg['From'] = SMTP_USER
        msg['To'] = addr
        msg['Subject'] = input("메일 제목을 입력해주세요 >> ")

        contents = input("메일 내용을 입력해주세요. >> ")
    
        # msg['text'] = contents
        text = MIMEText(_text = contents, _charset = 'utf-8')
        msg.attach(text)

        # SMTP로 접속할 서버 정보를 가진 클래스 변수를 생성한다.
        smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

        # 계정 정보로 로그인
        smtp.login(SMTP_USER, SMTP_PASSWORD)

        # 메일 발송
        smtp.sendmail(SMTP_USER, addr, msg.as_string())

        print("\n 메일이 전송되었습니다. \n")
    
    except:
        print("\n 이메일을 발송하는 데에 오류가 발생했습니다. \n")
    smtp.close()


get_name = input("받는 사람의 이름을 입력해주세요 : ")
get_email = input("받는 사람의 이메일 주소를 입력해주세요 : ")

for i in range(486):
    send_mail(get_name, get_email)
