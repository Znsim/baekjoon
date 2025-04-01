#두 자연수 A,B
A = []
B = 42
#A % B : A를 B로 나눈 나머지 이다. 
#ex) 7,14,27,38을 3으로 나눈 나머지는 1,2,0,2

#수 10개를 입력 받은 뒤,
for i in range (10):
   A.append(int(input()))

#이를 42로 나눈 나머지를 구한다.
rem = {num % B for num in A}

#그 다음 서로 다른 값이 몇개인지 풀력하는 프로그램을 작성하시오.
print(len(rem))