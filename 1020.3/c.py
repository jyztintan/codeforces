import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    found = None
    clash = False
    for i in range(n):
        if a[i] != -1 and b[i] != -1:
            total = a[i] + b[i]
            if found is None:
                found = total
            elif found != total:
                clash = True
                break
            
    if clash:
        print(0)
        continue

    if found is not None:
        if min(a) + k < found or max(a) > found:
            print(0)
        else:
            print(1)
        continue
            
    possibles = min(a) + k - max(a) + 1
    print(max(0, possibles))
        
        
