#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 5000, and s is a string of length n consisting of characters '+' and '-', where the i-th character represents a_i = 1 if s_i = '+' and a_i = -1 if s_i = '-'.
def func():
    for i in range(int(input())):
        s = int(input())
        
        e = input()
        
        P = 0
        
        M = 0
        
        for q in e:
            if q == '+':
                P += 1
            else:
                M += 1
        
        print(P - M)
        
    #State: All test cases have been processed, `i` equals the total number of test cases (input), `s` is an integer such that 1 ≤ `s` ≤ 1000, `e` is an empty string, `q` is not defined since `e` is empty, `P` is the total count of '+' characters across all strings `e` for all test cases, and `M` is the total count of '-' or any other characters in all strings `e` for all test cases.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `s` (1 ≤ `s` ≤ 1000) and a string `e` of length `n` (1 ≤ `n` ≤ 5000) containing characters '+' and '-'. For each test case, it counts the number of '+' characters and subtracts the number of '-' characters in `e`, then prints the result. After processing all test cases, the function ensures that all test cases have been handled, and the final output is the cumulative sum of these differences for all test cases.

