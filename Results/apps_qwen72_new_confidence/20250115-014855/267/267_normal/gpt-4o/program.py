def find_min_max(m, s):
    if s == 0:
        if m == 1:
            return "0 0"
        else:
            return "-1 -1"
    
    if s > 9 * m:
        return "-1 -1"
    
    # Find the minimum number
    min_num = [0] * m
    sum_s = s
    for i in range(m-1, -1, -1):
        if sum_s > 9:
            min_num[i] = 9
            sum_s -= 9
        else:
            min_num[i] = sum_s
            break
    
    if min_num[0] == 0:
        for i in range(1, m):
            if min_num[i] > 0:
                min_num[i] -= 1
                min_num[0] = 1
                break
    
    # Find the maximum number
    max_num = [0] * m
    sum_s = s
    for i in range(m):
        if sum_s > 9:
            max_num[i] = 9
            sum_s -= 9
        else:
            max_num[i] = sum_s
            break
    
    return ''.join(map(str, min_num)) + ' ' + ''.join(map(str, max_num))


# Read the input
m, s = map(int, input().split())

# Get the result
result = find_min_max(m, s)

# Print the result
print(result)
