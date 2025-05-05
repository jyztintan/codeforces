import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, l, r = map(int, input().split())

    right = 0
    while right < m and right < r:
        right += 1

    print(- (m - right), right)