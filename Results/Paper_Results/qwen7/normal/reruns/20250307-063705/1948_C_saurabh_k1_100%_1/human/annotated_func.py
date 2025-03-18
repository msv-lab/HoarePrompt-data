#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5 and n is even; the first line of each test case contains a string of length n consisting of characters '<' and/or '>'; the second line of each test case contains a string of length n consisting of characters '<' and/or '>'; there are no arrows pointing outside the grid; the sum of n over all test cases doesn't exceed 2 \cdot 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = input()
        
        b = input()
        
        for i in range(1, n, 2):
            if i + 1 < n and a[i] == b[i + 1] == '<' or a[i] == b[i - 1] == '<':
                print('No')
                break
        else:
            print('yes')
        
    #State: Output State: The loop will execute for all valid values of `t`, meaning it will run the inner loop for all integers from 1 to `n-1` with a step of 2. If during any iteration of the loop, the condition `a[i] == b[i+1] == '<'` or `a[i] == b[i-1] == '<'` is met, the loop will break and print 'No'. If the loop completes all its iterations without breaking, it will print 'yes'.
    #
    #In summary, after all iterations of the loop have finished, the output will be 'yes' if none of the conditions `a[i] == b[i+1] == '<'` or `a[i] == b[i-1] == '<'` are satisfied for any odd `i` in the range from 1 to `n-1`. Otherwise, if any of these conditions are met at any point, the output will be 'No'.
#Overall this is what the function does:The function processes a series of test cases, each containing an integer \( t \) (number of test cases), an integer \( n \) (length of two character strings), and two strings of length \( n \) consisting of characters '<' and '/>'. For each test case, it checks if any pair of characters in the same position (odd index) of the two strings satisfy specific conditions (`a[i] == b[i+1] == '<'` or `a[i] == b[i-1] == '<'`). If any such condition is met, it prints 'No' and stops processing further test cases. If no such conditions are met for any test case, it prints 'Yes'.

