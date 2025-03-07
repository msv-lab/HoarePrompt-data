#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 100, and a_1, a_2, a_3, \dots, a_n are integers such that 1 ≤ a_i ≤ 10^6.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        year = 0
        
        for ai in a:
            year += year % ai or ai
        
        print(year)
        
    #State: For each input integer \( t \), there will be \( t \) outputs, each being the result of the computation described in the loop body for the corresponding input list \( a \). Specifically, for each list \( a \), the output is the final value of the variable \( year \) after executing the inner loop. The value of \( year \) is calculated by starting with 0 and then for each element \( ai \) in \( a \), adding \( year \% ai \) or \( ai \) to \( year \).
#Overall this is what the function does:The function processes a series of test cases defined by an integer `t` (1 ≤ t ≤ 1000). For each test case, it reads an integer `n` (1 ≤ n ≤ 100) and a list of `n` integers `a_i` (1 ≤ a_i ≤ 10^6). It calculates the final value of `year`, which starts at 0 and is incremented by either `year % a_i` or `a_i` for each element `a_i` in the list. The function prints the final value of `year` for each test case.

