a, b, c = map(int, input().split())

if a == b == c:  # 세 숫자가 모두 같은 경우
    print(10000 + a * 1000)
elif a == b or a == c:  # 두 숫자가 같은 경우
    print(1000 + a * 100)
elif b == c:  # `b`와 `c`가 같은 경우
    print(1000 + b * 100)
else:  # 모두 다른 경우
    print(max(a, b, c) * 100)
