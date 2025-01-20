def cal_sum(n):
    if n < 0:
        return 0
    
    perrin = [3, 0, 2]
    
    for i in range(3, n+1):
        perrin.append(perrin[i-2] + perrin[i-3])
        
    return sum(perrin)

# Test cases
assert cal_sum(9) == 49
assert cal_sum(10) == 66
assert cal_sum(11) == 88
