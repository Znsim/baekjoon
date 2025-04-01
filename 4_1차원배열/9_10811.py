N,M = map(int,input().split())

#배열
a = [i for i in range(1,N+1)]
temp = 0

for i in range(M):
    i,j = map(int, input().split())
    temp = a[i-1:j]
    temp.reverse()
    a[i-1:j] = temp

for i in range(N):
    print(a[i],end=' ')