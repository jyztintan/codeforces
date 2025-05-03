import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    count = 0
    diff = 0
    for c in s:
        if c == '1':
            count += 1
            diff -= 1
        elif c == '0':
            diff += 1
        # print(diff)
    # print(count, diff)
    print(count * n + diff)
