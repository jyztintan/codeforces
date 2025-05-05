import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().split(" ")
    s = map(lambda x:x[0], s)
    print("".join(s))
