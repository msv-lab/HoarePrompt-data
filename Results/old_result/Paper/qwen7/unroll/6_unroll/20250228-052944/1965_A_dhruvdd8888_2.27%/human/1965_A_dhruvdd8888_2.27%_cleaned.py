rrr = randint(8888, 88888)

def func_1():
    N = int(input())
    nums = set(input().split())
    nums = sorted(map(int, nums))
    if len(nums) == 1:
        return print('Alice')
    if len(nums) == 2:
        return print('Bob')
    nums.insert(0, 0)
    cd = 0
    for i in range(len(nums) - 2):
        if nums[i + 1] - nums[i] == 1:
            cd += 1
        else:
            break
    if cd & 1:
        return print('Bob')
    else:
        return print('Alice')
for _ in range(int(input())):
    func_1()