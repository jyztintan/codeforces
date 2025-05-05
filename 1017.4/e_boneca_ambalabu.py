import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    bits = max(nums).bit_length()
    bit_count = [0] * bits

    for num in nums:
        bit_ptr = 0
        while num:
            bit_count[bit_ptr] += num & 1
            num >>= 1
            bit_ptr += 1

    best = 0
    for num in nums:
        test = 0
        for bit in range(bits):
            ones = bit_count[bit]
            zeroes = n - ones
            if num >> bit & 1:
                test += zeroes << bit
            else:
                test += ones << bit
        best = max(best, test)

    print(best)