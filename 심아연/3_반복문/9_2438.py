N = int(input())

for i in range(1, N+1):  # 1부터 N까지 반복
    for j in range(i):  # i개의 별 출력
        print("*", end="")  # 줄바꿈 없이 출력
    print()  # 줄바꿈
