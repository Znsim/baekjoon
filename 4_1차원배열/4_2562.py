aa = [int(input()) for i in range(9)]

max_value = max(aa)
max_index = aa.index(max_value)+1

print(max_value)
print(max_index)