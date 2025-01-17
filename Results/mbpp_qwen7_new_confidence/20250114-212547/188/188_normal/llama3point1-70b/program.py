def median_trapezium(*args):
    num_list = sorted([*args])
    n = len(num_list)
    if n % 2 == 0:
        median = (num_list[n//2 - 1] + num_list[n//2]) / 2
    else:
        median = num_list[n//2]
    return median
