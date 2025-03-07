rrr = randint(8888, 88888)

def func_1():
    N = int(input())
    nums = set(input().split())
    nums.add('0')
    nums = sorted(map(int, nums))
    ls = 0
    for i in range(len(nums)):
        nums[i] -= ls
        ls += nums[i]
    nw = True
    cw = True
    for i in range(len(nums) - 2, 0, -1):
        if nums[i] == 1:
            cw = not nw
        else:
            cw = True
        nw = cw
    if cw:
        print('Alice')
    else:
        print('Bob')
for _ in range(int(input())):
    func_1()