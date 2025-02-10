#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3⋅10^5, and a is a list of n integers where 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n. The sum of n over all test cases does not exceed 3⋅10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    st = set()
    for i in range(n):
        st.add(arr[i] + i + 1)
        
    #State: Output State: `i` is equal to `n`; `st` is a set containing the values `arr[0] + 1`, `arr[3] + 4`, and `arr[i-1] + i`.
    #
    #This means that after the loop has executed all its iterations, the variable `i` will be equal to `n`. The set `st` will contain all the values of `arr[i] + i + 1` for every `i` from 0 to `n-1`. Specifically, it contains `arr[0] + 1`, `arr[3] + 4`, and `arr[n-1] + n` (since `i` starts from 0 and goes up to `n-1`).
    print(*sorted(st, reverse=True))
    #This is printed: arr[3] + 4 arr[n-1] + n arr[0] + 1
#Overall this is what the function does:The function processes a list of integers `a` with length `n` and computes a set containing the values of each element in `a` plus its index plus one. After sorting this set in descending order, it prints these values.

