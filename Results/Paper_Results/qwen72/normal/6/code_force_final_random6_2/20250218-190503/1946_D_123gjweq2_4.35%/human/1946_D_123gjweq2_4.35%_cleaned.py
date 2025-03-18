def func_1(arr, x):

    def find_max(cur_arr, bit):
        if bit == -1:
            return len(cur_arr)
        new_arr = []
        xor = 0
        thing1 = 0
        for i in cur_arr:
            xor ^= i
            if not xor >> bit & 1:
                new_arr.append(xor)
                xor = 0
        if xor >> bit & 1:
            thing1 = -1
        else:
            thing1 = find_max(new_arr, bit - 1)
        if x >> bit & 1:
            return max(find_max(cur_arr, bit - 1), len(new_arr))
        else:
            return thing1
    return find_max(arr, 31)
testcases = range(int(input()))
for case in testcases:
    (n, k) = [int(i) for i in input().split(' ')]
    arr = [int(i) for i in input().split(' ')]
    print(func_1(arr, k))