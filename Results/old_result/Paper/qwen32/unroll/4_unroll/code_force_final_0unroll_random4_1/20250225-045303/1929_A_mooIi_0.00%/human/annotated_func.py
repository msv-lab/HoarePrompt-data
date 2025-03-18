#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = map(str, sorted(list(map(int, input().split()))))
        
        print(' '.join(ar))
        
    #State: t test cases have been processed, and for each test case, a sorted list of n integers (converted to strings and joined by spaces) has been printed. The variable t remains unchanged, and the variables n and ar are no longer in scope after the loop finishes.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of an integer `n` and a list of `n` integers. For each test case, it sorts the list of integers in ascending order, converts each integer to a string, joins them with spaces, and prints the resulting string. The function does not return any value; it only prints the output for each test case.

