n, k = map(int, input().split())
nums = list(map(int, input().split()))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

lcm = 1
for num in nums:
    lcm = lcm * num // gcd(lcm, num)

res = 0
for i in range(n):
    temp = lcm
    for j in range(i, n):
        temp = temp * nums[j] // gcd(temp, nums[j])
        if temp % k == 0:
            res += 1

print(res)
