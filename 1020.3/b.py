import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    ans = []
    if x >= n:
        ans = list(range(n))
    else:
        left = list(range(x))
        middle = list(range(n - 1, x,-1))
        ans = left + middle + [x]
    print(*ans)
    
