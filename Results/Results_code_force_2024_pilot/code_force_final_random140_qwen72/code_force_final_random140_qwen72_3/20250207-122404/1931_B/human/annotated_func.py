#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 2·10^5, representing the number of containers. a is a list of n integers where 0 ≤ a_i ≤ 10^9, representing the initial amounts of water in the containers. The sum of a_i in each test case does not exceed 2·10^9, and the sum of a_i is divisible by n. The sum of n over all test cases does not exceed 2·10^5.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        arr.sort()
        
        if all(arr[i] <= arr[i + 1] for i in range(n - 1)):
            print('YES')
        else:
            print('NO')
        
    #State: After all iterations, `t` is an input integer where 1 ≤ t ≤ 10^4, `_` has been incremented by the number of test cases executed (i.e., `_` is now equal to `t`), and for each test case, `n` was an input integer, and `arr` was a sorted list of integers read from the input. For each test case, if all elements in `arr` were in non-decreasing order, the program printed 'YES'; otherwise, it printed 'NO'. The values of `t`, `n`, and the elements of `arr` for each test case remain as described in the initial state.
#Overall this is what the function does:The function `func_1` reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` representing the number of containers, followed by a list of `n` integers representing the initial amounts of water in the containers. The function sorts the list of water amounts and checks if the list is in non-decreasing order. If the list is sorted, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function completes without returning any value. The final state includes the input values `t`, `n`, and the sorted lists of water amounts for each test case, with the results of the checks printed for each test case.

