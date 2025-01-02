INF = 987654321987654321987654321

def func_1(delimiter=' '):
    return map(int, raw_input().split(delimiter))

def func_2(delimiter=' '):
    return raw_input().split(delimiter)

def func_3(delimiter=' '):
    return map(float, raw_input().split(delimiter))

def func_4(a, x):
    """Locate the leftmost value exactly equal to x"""
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def func_5(a, x):
    """Find rightmost value less than x"""
    i = bisect_left(a, x)
    if i:
        return a[i - 1]
    raise ValueError

def func_6(a, x):
    """Find rightmost value less than or equal to x"""
    i = bisect_right(a, x)
    if i:
        return a[i - 1]
    raise ValueError

def func_7(a, x):
    """Find leftmost value greater than x"""
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def func_8(a, x):
    """Find leftmost item greater than or equal to x"""
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def func_9(a, x, left, right):
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        elif a[mid] > x:
            right = mid - 1
        pass
    return -1
    pass

def func_10(format, *args):
    """Format args with the first argument as format string, and write.
	Return the last arg, or format itself if there are no args."""
    sys.stdout.write(str(format) % args)
if __name__ == '__main__':
    (a, b, c, d) = func_1()
    prob_a = a / b
    prob_b = c / d
    prev = 0
    now = 0
    now += prob_a
    acc = (1 - prob_a) * (1 - prob_b)
    ii = 0
    while now - prev > 1e-07:
        prev = now
        ii += 1
        now += acc * prob_a
        acc *= (1 - prob_a) * (1 - prob_b)
        pass
    func_10('%.6f\n', now)
    pass