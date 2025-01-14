t = int(input())  # 테스트 케이스 개수 입력
results = []  # 결과를 저장할 리스트

# 입력받고 계산
for _ in range(t):
    a, b = map(int, input().split())
    results.append(a + b)  # 결과를 리스트에 추가

# 출력
for result in results:
    print(result)
