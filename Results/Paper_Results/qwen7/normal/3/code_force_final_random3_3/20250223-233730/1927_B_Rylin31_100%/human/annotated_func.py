#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and the second line contains n non-negative integers a_1, a_2, \dots, a_n such that 0 ≤ a_i < n.
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
        
    #State: Output State: The output state after the loop executes all the iterations is that `ans` is a string consisting of characters derived from the values of `s[j] + 97` for each `j` in `array`, where `s[j]` has been incremented by the number of times its index was encountered in `array`. The variable `i` will be equal to the total number of test cases, `s` will be a list of integers where each element `s[j]` is incremented by the count of how many times `j` appears in `array`, and `array` will be a list of integers as provided by the input. The final `ans` will be constructed by concatenating characters based on the updated values in `s`.
    #
    #In simpler terms, `ans` will be a string made up of characters from the alphabet (starting from 'a' to 'z') based on how many times each index in `array` appears, and `s` will reflect the cumulative count of these appearances for each index.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer \( t \) indicating the number of subsequent test cases, then reads another integer \( n \) and a list of \( n \) non-negative integers. It constructs a string `ans` by converting the values of `s[j] + 97` to characters from the alphabet ('a' to 'z'), where `s[j]` is incremented by the count of how many times `j` appears in the list. After processing all test cases, it prints the constructed strings `ans` for each case.

