l, k = map(lambda i: int(i), raw_input().split(' '))
candy_list = map(lambda i: int(i), raw_input().split(' '))

def max_boxes(k, candy_array):
    res_map = {}
    res = 0
    for candy in candy_array:
        if res_map.has_key(k - candy % k) and res_map[k - candy % k] > 0:
            res += 2
            res_map[k - candy % k] = res_map[k - candy % k] - 1
        else:
            res_map[candy % k] = res_map[candy % k] + 1 if res_map.has_key(candy % k) else 1
    print(res)

max_boxes(k, candy_list)
