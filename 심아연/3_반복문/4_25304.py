#금액 X
x = int(input())
#물건 종류의 수 Y
y = int(input())

sum = 0

for i in range(2,2+y):
    a,b = map(int,input().split())
    sum += a*b

if sum ==x:
    print("Yes")
else :
    print("No")