#State of the program right berfore the function call: The input consists of t test cases (1 ≤ t ≤ 10^4). For each test case, the first line contains an integer n (1 ≤ n ≤ 2 · 10^5), the length of the permutation p and the array a. The second line contains n integers a_1, a_2, ..., a_n (-n ≤ a_i ≤ n), the elements of array a. The sum of n over all test cases does not exceed 2 · 10^5. It is guaranteed that there is at least one valid permutation p for the given data.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    mex = []
    minn = 0
    used = {}
    for i in range(n):
        if arr[i] > 0:
            mex.append(minn)
            used[minn] = True
            while minn in used:
                minn += 1
        else:
            mex.append(abs(arr[i] - minn))
            used[abs(arr[i] - minn)] = True
        
    #State: mex: [calculated values based on arr], minn: smallest unused non-negative integer, used: {dict of used integers}
    for itm in mex:
        print(itm, end=' ')
        
    #State: mex: [calculated values based on arr], minn: smallest unused non-negative integer, used: {dict of used integers}
    print()
    #This is printed: (newline)
#Overall this is what the function does:The function `func_1` processes each test case consisting of an integer `n` and an array `a` of `n` integers. For each test case, it calculates a sequence of integers `mex` based on the values in `a` and prints this sequence. The sequence `mex` is derived such that for each positive element in `a`, it appends the smallest unused non-negative integer to `mex`, and for each non-positive element, it appends the absolute difference between the element and the smallest unused non-negative integer. After processing each test case, it prints the sequence `mex` followed by a newline.

