#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 3 · 10^5, representing the length of the array a. The array a consists of n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 3 · 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    st = set()
    for i in range(n):
        st.add(arr[i] + i + 1)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer such that 1 ≤ n ≤ 3 · 10^5, `arr` is a list of `n` integers read from the input, each integer in `arr` is between 1 and 10^9, and the sum of `n` over all test cases does not exceed 3 · 10^5, `st` is a set containing the values `arr[i] + i + 1` for all `i` from 0 to `n-1`, `i` is `n-1`.
    print(*sorted(st, reverse=True))
    #This is printed: [sorted elements of st in descending order]
#Overall this is what the function does:The function reads an integer `n` and a list of `n` integers from the input. It then computes a set of values where each value is the sum of an element from the list and its index plus one. Finally, it prints the elements of this set in descending order. The function is designed to handle multiple test cases, each defined by a new input of `n` and a corresponding list of integers. After processing each test case, the function outputs the sorted set of computed values.

