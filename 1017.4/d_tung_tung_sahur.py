import sys
input = sys.stdin.readline

def segment(s):
    ans = []
    prev = s[0]
    count = 0
    for i in range(len(s)):
        if s[i] != prev:
            ans.append(count)
            prev = s[i]
            count = 1
        else:
            count += 1
    ans.append(count)
    return ans

t = int(input())
for _ in range(t):
    original = input().strip()
    check = input().strip()

    if original[0] != check[0]:
        print("NO")
        continue

    ori_segments = segment(original)
    check_segments = segment(check)

    if len(ori_segments) != len(check_segments):
        print("NO")
        continue

    valid = True
    for i in range(len(ori_segments)):
        if ori_segments[i] > check_segments[i] or check_segments[i] > 2 * ori_segments[i]:
            valid = False
            break

    if not valid:
        print("NO")
    else:
        print("YES")

