#State of the program right berfore the function call: 
def func_1():
    s = list(map(int, input().split()))
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 1:
            n += 1
        
        if s[i] == 0 and n != 0:
            ans += n + 1
        
    #State: Output State: The final output state after the loop executes all iterations will be a list `s` of integers entered by the user, `n` is equal to the length of the list `s`, and `ans` is the sum of `n + 1` for each occurrence where an element in `s` is 0 and there was a previous non-zero element (i.e., `n` was greater than 0).
    #
    #In more detail, if during the loop's execution, there were `k` instances where an element in `s` was 0 and `n` was not 0 before that, then `ans` will be `n + k`. If no such instances occurred, `ans` will remain 0. The variable `i` will be equal to the length of the list `s` after the loop completes.
    print(ans)
    #This is printed: ans (where ans is the sum of n + 1 for each occurrence where an element in s is 0 and there was a previous non-zero element)
#Overall this is what the function does:The function reads a list of integers from the user input, counts the number of consecutive non-zero elements, and calculates the sum of 1 plus the count of non-zero elements immediately preceding each zero in the list. This sum is then printed as the final output. The function does not accept any parameters and does not return any value.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, the input is a binary string s where 2 <= len(s) <= 2 * 10^5 and s consists only of '0' and '1'.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: Output State: `t` must be greater than 0.
    #
    #Natural Language Explanation: The loop continues to execute as long as `t` is greater than 0. Since the condition for executing the loop does not change with each iteration (it always checks if `t > 0`), and we know it executes at least 3 times with this condition being true, it implies that `t` was initially greater than 0 and remained so throughout all iterations. Therefore, after all iterations of the loop have finished, `t` must still be greater than 0.
#Overall this is what the function does:The function processes an unspecified number of test cases, each represented by a binary string. After processing all test cases, it ensures that the variable `t` (representing the number of test cases) remains greater than 0.

