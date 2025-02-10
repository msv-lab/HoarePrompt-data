def func_1(arr, x):

    def find_new(cur_arr, bit):
        if bit == -1:
            return len(cur_arr)
        new_arr = []
        xor = 0
        for i in cur_arr:
            xor ^= i
            if not xor >> bit & 1:
                new_arr.append(xor)
                xor = 0
        if xor >> bit & 1:
            thing1 = -1
        else:
            thing1 = len(new_arr)
        if x >> bit & 1:
            return max(thing1, find_new(cur_arr, bit - 1))
        elif thing1 != -1:
            return find_new(new_arr, bit - 1)
        return -1
    return find_new(arr, 30)
testcases = range(int(input()))
for case in testcases:
    (n, k) = [int(i) for i in input().split(' ')]
    arr = [int(i) for i in input().split(' ')]
    print(func_1(arr, k))