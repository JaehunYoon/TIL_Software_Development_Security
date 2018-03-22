# sort

res1 = ['e', 'a', 'h']
res2 = [1, 6, 2]
res1.sort()
res2.sort(reverse=True)  # True 라고 정확히 입력해야 함

print(res1)
print(res2)

res3 = sorted(res1)  # 외부정렬
res4 = sorted(res1, reverse=True)

print(res1)
print(res2)
print(res3)
print(res4)

# sort 함수로는 딕셔너리 정렬이 불가능하지만, sorted 는 딕셔너리 정렬이 가능하다.

a = {'2': 'B', '1': 'A', '3': 'U'}
a1 = sorted(a)
print(a1)
a1.reverse()  # 반환값이 없는 함수이다.
print(a1)
