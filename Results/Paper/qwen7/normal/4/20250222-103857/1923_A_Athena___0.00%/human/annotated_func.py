#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and a list of n integers a (a[i] is either 0 or 1) representing the state of each cell (0 for free, 1 for chip). Additionally, in each test case, at least one cell contains a chip.
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
        
    #State: Output State: After all iterations of the loop have finished, `t` will be 0, as it decreases by 1 with each iteration until it reaches 0. `n` will retain its original value since it is not modified within the loop. `a` will be an empty list if all inputs resulted in lists with only zeros or no valid input was provided, otherwise, `a` will contain the remaining non-zero elements from the last input list after removing all leading and trailing zeros. `res` will be the total count of zeros found in all the lists processed during the loop iterations. The variable `i` will be equal to the length of the final list `a`, indicating that the loop has completed all its iterations on all provided inputs.
    #
    #This means that after processing all inputs, `t` will be 0, `n` will be the original input, `a` will be either an empty list or a list of non-zero integers, `res` will be the cumulative count of zeros from all inputs, and `i` will reflect the length of the final list `a`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` (number of test cases), an integer `n` (length of the list), and a list `a` of `n` integers (each either 0 or 1). For each test case, it removes leading and trailing zeros from the list `a`. Then, it counts the number of zeros remaining in the list and prints the list followed by the zero count. After processing all test cases, the function outputs the final state where `t` is 0, `n` retains its original value, `a` is either empty or contains the remaining non-zero elements, `res` is the total count of zeros from all test cases, and `i` reflects the length of the final list `a`.

