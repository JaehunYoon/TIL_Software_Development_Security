# get

a = {'q': 123, 'w': 456}
res = a.get('q')
print(res)
print(a['q'])

# 두 출력의 차이는? => get 함수를 쓸 때 키가 없는 값을 찾으면 none
# 그냥 딕셔너리에서 키 값으로 찾았을 때 없으면 오류

res = a.get('t', "holy shit")
print(res)
