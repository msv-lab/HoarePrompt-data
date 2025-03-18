#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, m_1, m_2 are positive integers such that 1 ≤ m_1, m_2 ≤ n ≤ 2⋅10^5. p_1, p_2, ..., p_{m_1} are strictly increasing integers such that 1 ≤ p_i ≤ n. s_1, s_2, ..., s_{m_2} are strictly increasing integers such that 1 ≤ s_i ≤ n.
def func_1():
    N, M1, M2 = map(int, input().split())
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))
    if (L[-1] != R[0]) :
        return 0
        #The program returns 0
    #State: t is a positive integer such that 1 ≤ t ≤ 10^4, N is an input integer, M1 is an input integer, M2 is an input integer, R is a list of integers obtained from splitting the input string and converting each element to an integer, and L[-1] is equal to R[0]
    if (L[0] != 1 or R[0] != N) :
        return 0
        #The program returns 0
    #State: t is a positive integer such that 1 ≤ t ≤ 10^4, N is an input integer, M1 is an input integer, M2 is an input integer, R is a list of integers obtained from splitting the input string and converting each element to an integer, and L[-1] is equal to R[0], L[0] is 1 and R[0] is equal to N
    if (M1 > 1 and M2 > 1 and L[-2] == R[1]) :
        return 0
        #The program returns 0
    #State: t is a positive integer such that 1 ≤ t ≤ 10^4, N is an input integer, M1 is an input integer, M2 is an input integer, R is a list of integers obtained from splitting the input string and converting each element to an integer, and L[-1] is equal to R[0], L[0] is 1 and R[0] is equal to N, M1 is less than or equal to 1 or M2 is less than or equal to 1 or L[-2] is not equal to R[1]
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
            
        #State: Output State: `ans` is the result of multiplying `ans` by `nums_left` modulo `MOD` for each `i` from `L[-1] - 1` down to 2, where `cur` is decremented when `i` equals `L[cur]`, and `nums_left` and `i` are decremented in each iteration. The final value of `ans` after the loop completes will be the product of `ans` and `nums_left` for each `i` from `L[-1] - 1` down to 2, under the modulo operation with `MOD`.
        #
        #To break it down further:
        #- Initially, `ans` is set to `math.comb(N - 1, L[-1] - 1)`.
        #- `cur` starts at `M1 - 2`.
        #- `nums_left` starts at `L[-1] - 2`.
        #- `i` starts at `L[-1] - 1`.
        #
        #For each iteration of the loop:
        #- If `i` equals `L[cur]`, then `cur` is decremented.
        #- Otherwise, `ans` is updated by multiplying it with `nums_left` modulo `MOD`.
        #- Both `nums_left` and `i` are decremented by 1.
        #
        #After the loop completes, `ans` will hold the final computed value based on the described operations.
    #State: `ans` is the result of `math.comb(N - 1, L[-1] - 1)` multiplied by `nums_left` modulo `MOD` for each `i` from `L[-1] - 1` down to 2, under the condition that `M1 > 1`. If `M1 <= 1`, then `ans` remains as the initial value `math.comb(N - 1, L[-1] - 1)`.
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
            
        #State: Output State: `cur` is `R.count(R[0]) + 1`, `nums_left` is `0`, `ans` is the initial value `math.comb(N - 1, L[-1] - 1)` if `M1 <= 1`, otherwise `ans` is the result of `math.comb(N - 1, L[-1] - 1)` multiplied by `nums_left` (which is 0) modulo `MOD` for each `i` from `L[-1] - 1` down to 2, and `i` is `R[0] + 1`.
        #
        #Explanation: The loop iterates from `i = 0` to `i = N-1`. In each iteration, if `i` equals `R[cur]`, `cur` increments by 1. Otherwise, `ans` is updated by multiplying it with `nums_left` and taking modulo `MOD`. `nums_left` decreases by 1 in every iteration. Since `nums_left` starts at `N - R[0] - 1` and decreases by 1 until it reaches 0, the final value of `nums_left` will be 0 after `N - R[0]` iterations. The value of `cur` will increment once for each occurrence of `R[cur]` within the range `[0, N-1]`, plus the initial value of 1, resulting in `cur` being `R.count(R[0]) + 1`. Since `nums_left` becomes 0, any further multiplications involving it will result in `ans` remaining unchanged.
    #State: `nums_left` is 0, `cur` is `R.count(R[0]) + 1`, and `ans` remains as the initial value `math.comb(N - 1, L[-1] - 1)` if `M1 <= 1`, otherwise `ans` is the result of `math.comb(N - 1, L[-1] - 1)` multiplied by `nums_left` (which is 0) modulo `MOD` for each `i` from `L[-1] - 1` down to 2.
    return ans
    #The program returns 0
#Overall this is what the function does:The function reads input values for `N`, `M1`, `M2`, `L`, and `R`, and checks several conditions. If any of these conditions are not met, the function returns 0. Otherwise, it calculates a value using combinatorial mathematics and specific rules based on the input lists `L` and `R`, and returns this calculated value. If none of the conditions are violated, the function ultimately returns a value derived from combinatorial calculations and specific list operations, or 0 if conditions are not satisfied.

