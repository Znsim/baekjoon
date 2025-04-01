all_s = set(range(1,31))

submitted_s = set()

for _ in range(28):
    num = int(input())
    submitted_s.add(num)

missing_s = sorted(all_s - submitted_s)

print(missing_s[0])
print(missing_s[1])