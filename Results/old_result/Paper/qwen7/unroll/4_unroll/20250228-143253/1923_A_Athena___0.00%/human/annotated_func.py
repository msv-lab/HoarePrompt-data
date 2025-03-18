#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000; for each test case, n is an integer such that 2 ≤ n ≤ 50; the second line of each test case contains n integers a_1, a_2, ..., a_n where each a_i is either 0 or 1, indicating whether the i-th cell is free (0) or contains a chip (1); in each test case, at least one cell contains a chip.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        res = 0
        
        while a and a[0] == 0:
            a.pop(0)
        
        while a and a[-1] == 0:
            a.pop()
        
        print(a)
        
        for i in range(len(a)):
            if a[i] == 0:
                res += 1
        
        print(res)
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 1000, and for each iteration of the loop, the list `a` has had all leading and trailing zeros removed, and the variable `res` holds the count of zeros in the final list `a`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer t (number of test cases), an integer n (length of the list), and a list of n integers a (indicating free cells with 0 and cells with chips with 1). For each test case, it removes all leading and trailing zeros from the list a, counts the remaining zeros, and prints the modified list followed by the count of zeros. The function does not return any value but prints the results for each test case.

