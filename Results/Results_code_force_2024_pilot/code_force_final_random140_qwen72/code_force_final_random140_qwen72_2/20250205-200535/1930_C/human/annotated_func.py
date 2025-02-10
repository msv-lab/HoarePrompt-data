#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 3 · 10^5, representing the length of the array a. The array a consists of n integers where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 3 · 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    st = set()
    for i in range(n):
        st.add(arr[i] + i + 1)
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `n` is an input integer where 1 ≤ n ≤ 3 · 10^5, `a` is a list of `n` integers where 1 ≤ a_i ≤ 10^9, `arr` is a list of integers read from input, `st` contains the values `arr[i] + i + 1` for each `i` from 0 to `n-1`, `i` is `n-1`.
    print(*sorted(st, reverse=True))
    #This is printed: [values of st sorted in descending order]
#Overall this is what the function does:The function reads an integer `n` and a list of `n` integers from the input. It then computes a set `st` containing the values `arr[i] + i + 1` for each index `i` from 0 to `n-1`. Finally, it prints the elements of `st` sorted in descending order. The function processes multiple test cases, each defined by an integer `n` and a list of integers, and prints the results for each test case.

