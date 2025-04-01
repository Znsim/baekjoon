N,M = map(int,input().split())
basket = [1] * N


for x in range(M):
    i,j = map(int,input().split())
    basket[i-1],basket[j-1] = basket[j-1],basket[i-1]

print(*basket)