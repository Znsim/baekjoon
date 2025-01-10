a = int(input())
# / 나누기
# % 나머지
if(a%4 ==0 and a%100 != 0 ) or(a % 400 == 0):
    print("1")
else:
    print("0")