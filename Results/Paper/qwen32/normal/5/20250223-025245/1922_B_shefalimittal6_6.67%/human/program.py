import math
 
t = int(input())
for _ in range(t):
    n = int(input())
    num_of_lens = {}
    nums = list(map(int, input().split()))
    for x in nums:
        num_of_lens[x] = num_of_lens.get(x, 0) + 1
 
    res = 0
    for cnt in num_of_lens.values():
        if cnt >= 3:
            res += math.comb(cnt, 3)
        if cnt >= 2:
            total_sum = sum(i for i in num_of_lens.values() if i!= cnt)
            res += math.comb(cnt, 2) * total_sum
 
    print(res)