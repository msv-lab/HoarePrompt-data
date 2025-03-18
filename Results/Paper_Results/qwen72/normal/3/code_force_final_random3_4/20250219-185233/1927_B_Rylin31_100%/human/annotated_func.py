#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5, and for each test case, a valid string s exists.
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
        
    #State: The loop has executed `t` times, where `t` is an integer such that 1 ≤ t ≤ 10^4. For each of the `t` test cases, `l` is an input integer greater than 0, `s` is a list of length `l` initialized to 0, `array` is a list of integers provided by the user, and `ans` is a string containing the characters corresponding to the ASCII values of the elements in `s` at the indices specified by `array` plus 97, concatenated in the order the indices appear in `array`. After all iterations, `i` has reached the value of `t`, and all test cases have been processed, with the final `ans` string printed for each test case.
#Overall this is what the function does:The function `func` processes a series of test cases. It reads an integer `t` from the input, indicating the number of test cases. For each test case, it reads an integer `l` and a list of integers `array` from the input. It then constructs a string `ans` by mapping each integer in `array` to a character in the alphabet (starting from 'a') based on the current count in a list `s` of length `l`. After processing all integers in `array`, it prints the resulting string `ans`. The function does not return any value; it only prints the results for each test case.

