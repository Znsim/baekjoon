import sys
dial = {
    'ABC': 3,
    'DEF': 4,
    'GHI': 5,
    'JKL': 6,
    'MNO': 7,
    'PQRS': 8,
    'TUV': 9,
    'WXYZ': 10
}

di = input()
time =0 

for i in di:
    for k in dial:
        if i in k :
            time += dial[k]

print(time)