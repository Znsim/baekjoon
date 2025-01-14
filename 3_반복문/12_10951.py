import sys

for line in sys.stdin:  # 입력이 더 이상 없을 때까지 읽기
    a, b = map(int, line.split())
    print(a + b)
