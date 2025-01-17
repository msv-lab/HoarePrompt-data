def fixed_ops(a):
    """
    turn a into [0,1,2, ..., n-1]
    """
    n = len(a)
    if n == 1:
        if a[0] == 0:
            return []
        else:
            return [[1, 1]]
    ops = []

    first_ops = fixed_ops(a[:n-1])
    for op in first_ops:
        ops.append(op)
    
    if a[n-1] == n-1:
        return ops
    else:
        ops.append([1, n])
        for op in first_ops:
            ops.append(op)
    return ops


def solve(a):
    max_sum = 0
    ops = []
    n = len(a)
    if n == 0:
        return 0, []
    if n == 1:
        if a[0] == 0:
            return 1, [[1, 1]]
        else:
            return a[0], []

    # Can be reduced to smaller problem, using DP
    # find the largest element larger than n
    # if yes, then divide and merge
    # if no, then return fixed strategy
    max_elem = -1
    max_elem_idx = 0
    for i in range(len(a)):
        max_elem = max(max_elem, a[i])
        if max_elem == a[i]:
            max_elem_idx = i
    if max_elem <= n:
        temp_ops = fixed_ops(a)
        for op in temp_ops:
            ops.append(op)
        ops.append([1, n])
        return n**2, ops
    i = max_elem_idx
    left_sum, left_ops = solve(a[:i]) 
    right_sum, right_ops = solve(a[i+1:])
    add_on = n - i - 1
    for op in right_ops:
        op[0] += add_on
        op[1] += add_on

    max_sum = left_sum + a[i] + right_sum
    for op in left_ops:
        ops.append(op)
    for op in right_ops:
        ops.append(op)

    return max_sum, ops


def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_sum, ops= solve(a)
    n_ops = len(ops)
    print(max_sum, n_ops)
    for op in ops:
        print(op[0], op[1])

if __name__ == "__main__":
    main()