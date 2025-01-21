#문제
#총 N개의 정수가 주어 졌을 때, 정수 v가 몇 개인지 구하는 프로그램

#입력
#첫 줄에 정수의 개수 N(1<= N <= 100)이 주어진다.
#둘째 줄에는 정수가 공백으로 구분되어있다.
#셋째 줄에는 찾으려 하는 정수 v가 주어진다. 

#출력
#첫재 줄에 입력으로 주어진 N개의 정수 중에 v가 몇개 인지 출력한다.

N = int(input())
aa = list(map(int,input().split()))
num = int(input())
count = 0

for i in range(0,N):
    if num == aa[i] :
        count += 1

print(count)