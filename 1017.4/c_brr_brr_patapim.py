import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    missing = set(range(1, 2 * n + 1))
    ans = []

    for i in range(n - 1):
        num, *_ = map(int, input().split())
        ans.append(num)
        missing.remove(num)

    suffix = map(int, input().split())
    for num in suffix:
        ans.append(num)
        missing.remove(num)

    ans = [missing.pop()] + ans
    print(' '.join(map(str, ans)))