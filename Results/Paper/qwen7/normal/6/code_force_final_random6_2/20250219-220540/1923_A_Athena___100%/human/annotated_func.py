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
        
        for i in range(len(a)):
            if a[i] == 0:
                res += 1
        
        print(res)
        
    #State: Output State: The list `a` has had all its trailing zeros removed, and the variable `res` contains the total count of trailing zeros that were removed.
    #
    #Explanation: After the loop has executed all its iterations, the value of `res` will be the total count of trailing zeros in the list `a`. The loop processes each input list `a` by removing leading and trailing zeros. Since the loop runs until all elements are processed, `res` will hold the count of trailing zeros that were present in the original list `a`.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer t (number of test cases), an integer n (length of the list), and a list of n integers representing cells (0 for free, 1 for containing a chip). It removes all leading and trailing zeros from the list and counts the number of trailing zeros removed. The function then prints this count for each test case. If no cells contain a chip (all values are 0), it does not return any specific value for that case.

