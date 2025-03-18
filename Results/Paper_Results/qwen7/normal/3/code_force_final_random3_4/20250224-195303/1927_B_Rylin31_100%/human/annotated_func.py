#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and a is a list of n non-negative integers where 0 ≤ a_i < n.
def func():
    for i in range(int(input())):
        l = int(input())
        
        s = [(0) for i in range(l)]
        
        array = list(map(int, input().split()))
        
        ans = ''
        
        for j in array:
            ans += chr(s[j] + 97)
            s[j] += 1
        
        print(ans)
        
    #State: The final value of `ans` will be a string composed of characters derived from the list `s`. Each character in `ans` corresponds to `s[j] + 97` for each `j` in the original `array`, where `s[j]` is incremented by the number of times `j` appears in `array` across all iterations of the loop. The list `s` will have each of its elements incremented by the total number of times the loop executed. The variable `i` will be equal to the number of test cases, `input_value` will be greater than or equal to the number of test cases, `l` will be the length of the input list for the current test case, and the initial state of `s` will be unchanged.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer \( n \), followed by a list of \( n \) non-negative integers. It then constructs a string \( ans \) by converting each integer in the list to a corresponding character based on the value of the integer plus 97, and increments a separate list \( s \) by the count of each integer in the list. After processing all test cases, it prints the constructed string \( ans \) for each case. The final state includes the printed strings for all test cases.

