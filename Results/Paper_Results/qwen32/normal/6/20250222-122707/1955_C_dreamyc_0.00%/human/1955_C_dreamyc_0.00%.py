from collections import deque
T = int(input())
 
def solve(n,k,nums):
    nums = deque(nums)
    ans = 0
    while k and len(nums) >= 2:
        a , b = nums.popleft()  , nums.pop()
        x = min(a,b)
        if k >= 2 * x:
            a -= x
            b -= x
            k -= 2 * x
        else:
            break
        if a > 0:
            nums.appendleft(a)
        else:
            ans += 1
        if b > 0:
            nums.append(b)
        else:
            ans += 1
    if k and len(nums) == 1 and k >= nums[0]:
        return ans + 1
    return ans
 
for _ in range(T):
    n, k = list(map(int, input().split(' ')))
    nums = list(map(int, input().split(' ')))
    ans = solve(n,k,nums)
    print(ans)