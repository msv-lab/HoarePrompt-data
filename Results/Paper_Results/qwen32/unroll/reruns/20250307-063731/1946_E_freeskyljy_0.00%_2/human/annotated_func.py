#State of the program right berfore the function call: For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, m1 and m2 are integers such that 1 ≤ m1, m2 ≤ n. The arrays p and s contain m1 and m2 integers respectively, representing the indices of prefix and suffix maximums in increasing order, with each index being an integer between 1 and n inclusive. The sum of n across all test cases does not exceed 2 · 10^5.
def func_1():
    N, M1, M2 = map(int, input().split())
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))
    if (L[-1] != R[0]) :
        return 0
        #The program returns 0.
    #State: `N` is an integer such that 1 ≤ N ≤ 2 · 10^5, `M1` and `M2` are integers such that 1 ≤ M1, M2 ≤ N, the arrays `p` and `s` contain `M1` and `M2` integers respectively, representing the indices of prefix and suffix maximums in increasing order, with each index being an integer between 1 and N inclusive; `L` is a list of integers obtained from the input; `R` is a list of integers obtained from the input. Additionally, the last element of `L` is equal to the first element of `R`.
    if (L[0] != 1 or R[0] != N) :
        return 0
        #The program returns 0.
    #State: `N` is an integer such that 1 ≤ N ≤ 2 · 10^5, `M1` and `M2` are integers such that 1 ≤ M1, M2 ≤ N, the arrays `p` and `s` contain `M1` and `M2` integers respectively, representing the indices of prefix and suffix maximums in increasing order, with each index being an integer between 1 and N inclusive; `L` is a list of integers obtained from the input; `R` is a list of integers obtained from the input. Additionally, the last element of `L` is equal to the first element of `R`. The first element of `L` is 1 and the first element of `R` is N.
    if (M1 > 1 and M2 > 1 and L[-2] == R[1]) :
        return 0
        #The program returns 0
    #State: `N` is an integer such that 1 ≤ N ≤ 2 · 10^5, `M1` and `M2` are integers such that 1 ≤ M1, M2 ≤ N, the arrays `p` and `s` contain `M1` and `M2` integers respectively, representing the indices of prefix and suffix maximums in increasing order, with each index being an integer between 1 and N inclusive; `L` is a list of integers obtained from the input; `R` is a list of integers obtained from the input. Additionally, the last element of `L` is equal to the first element of `R`. The first element of `L` is 1 and the first element of `R` is N. Either `M1` is 1, or `M2` is 1, or `L[-2]` is not equal to `R[1]`.
    ans = math.comb(N - 1, L[-1] - 1)
    cur = M1 - 2
    if (M1 > 1) :
        nums_left = L[-1] - 2
        i = L[-1] - 1
        while i > 1:
            if i == L[cur]:
                cur -= 1
            else:
                ans = ans * nums_left % MOD
            
            nums_left -= 1
            
            i -= 1
            
        #State: `i` is 1, `cur` is `M1 - 2 - k`, `nums_left` is `N - L[-1] + k`, `ans` is the result of the multiplication and modulo operations performed during the loop.
    #State: `N` is an integer such that 1 ≤ N ≤ 2 · 10^5, `M1` and `M2` are integers such that 1 ≤ M1, M2 ≤ N, the arrays `p` and `s` contain `M1` and `M2` integers respectively, representing the indices of prefix and suffix maximums in increasing order, with each index being an integer between 1 and N inclusive; `L` is a list of integers obtained from the input; `R` is a list of integers obtained from the input. Additionally, the last element of `L` is equal to the first element of `R`. The first element of `L` is 1 and the first element of `R` is N. Either `M1` is 1, or `M2` is 1, or `L[-2]` is not equal to `R[1]`. If `M1` > 1, then `i` is 1, `cur` is `M1 - 2 - k`, `nums_left` is `N - L[-1] + k`, and `ans` is the result of the multiplication and modulo operations performed during the loop. If `M1` is 1, then `cur` remains `M1 - 2`.
    nums_left = N - R[0] - 1
    if (M2 > 1) :
        cur = 1
        i = R[0] + 1
        while i < N:
            if i == R[cur]:
                cur += 1
            else:
                ans = ans * nums_left % MOD
            
            nums_left -= 1
            
            i += 1
            
        #State: cur=1, nums_left=-1, ans=initial_value_of_ans
    #State: `N` is an integer such that 1 ≤ N ≤ 2 · 10^5, `M1` and `M2` are integers such that 1 ≤ M1, M2 ≤ N, the arrays `p` and `s` contain `M1` and `M2` integers respectively, representing the indices of prefix and suffix maximums in increasing order, with each index being an integer between 1 and N inclusive; `L` is a list of integers obtained from the input; `R` is a list of integers obtained from the input. Additionally, the last element of `L` is equal to the first element of `R`. The first element of `L` is 1 and the first element of `R` is N. Either `M1` is 1, or `M2` is 1, or `L[-2]` is not equal to `R[1]`. If `M1` > 1, then `i` is 1, `cur` is `M1 - 2 - k`, `nums_left` is `-1`, and `ans` is the result of the multiplication and modulo operations performed during the loop. If `M1` is 1, then `cur` remains `M1 - 2`. `nums_left` is `-1`. If `M2` > 1, then `cur` is set to 1 and `nums_left` is set to -1. If `M2` is 1, then `cur` and `nums_left` remain unchanged.
    return ans
    #The program returns the value of `ans`, which is the result of the multiplication and modulo operations performed during the loop.
#Overall this is what the function does:The function `func_1` reads input values for `N`, `M1`, `M2`, `L`, and `R`. It checks specific conditions involving the elements of `L` and `R` and returns 0 if any of these conditions are met. If none of the conditions are met, it calculates a value `ans` through a series of multiplication and modulo operations and returns this value.

