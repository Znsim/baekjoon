T = int(input())


for i in range(T):
    R,S = map(str,input().split())
    re = ""
    for j in range(len(S)):
        re += S[j] * int(R)
        
    print(re)