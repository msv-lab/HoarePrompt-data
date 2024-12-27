n = int(raw_input())
nums = [0] * n
for i in range(n):
    nums[i] = int(raw_input())

p = [1, 2]
np = 3
ok = True
for i in range(n):
    if np == nums[i]:
        ok = False
        break

    p.remove(nums[i])
    k = [nums[i], np]
    np = p[0]
    p = k

if ok:
    print("YES")
else:
    print("NO")
