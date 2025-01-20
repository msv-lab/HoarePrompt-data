#State of the program right berfore the function call: The input string consists only of lowercase Latin letters, «*», and «?». The string length does not exceed 200. The integer \( k \) is such that \( 1 \leq k \leq 200 \).
def func():
    s = input()

k = int(input())

ans = []

i = 0
    while i < len(s) and len(ans) < k:
        if s[i].isalpha():
            ans.append(s[i])
            if i + 1 < len(s) and s[i + 1] == '?':
                i += 2
            elif i + 1 < len(s) and s[i + 1] == '*':
                while i + 1 < len(s) and s[i + 1] == '*':
                    ans.append(s[i])
                    i += 2
                i += 1
            else:
                i += 1
        else:
            i += 1
        
    #State of the program after the loop has been executed: To determine the output state after all executions of the loop have finished, let's analyze the given loop and its behavior in detail.
    #
    #### Step-by-Step Analysis
    #
    #1. **Initial State**: 
    #   - `s` is an input string.
    #   - `k` is an integer such that \(1 \leq k \leq 200\).
    #   - `ans` is a list containing the first `k` characters of `s`.
    #   - `i` is initialized to `k`.
    #
    #2. **Loop Behavior**:
    #   - The loop continues as long as `i < len(s)` and `len(ans) < k`.
    #   - Inside the loop:
    #     - If `s[i]` is an alphabetic character:
    #       - If `s[i + 1] == '?'`, append `s[i + 2]` to `ans` and increment `i` by 2.
    #       - If `s[i + 1] == '*'`, keep appending `s[i]` to `ans` while `s[i + 1] == '*'`, then increment `i` by 1.
    #       - Otherwise, simply increment `i` by 1.
    #     - If `s[i]` is not an alphabetic character, increment `i` by 1.
    #
    #3. **Invariants and Variables**:
    #   - `ans` is built by appending alphabetic characters from `s`.
    #   - `i` is incremented based on the conditions inside the loop.
    #   - `k` remains constant throughout the loop.
    #
    #4. **Final State**:
    #   - The loop terminates when `i >= len(s)` or `len(ans) == k`.
    #   - The final value of `i` will be the minimum of `len(s)` and `k + 2 * n` where `n` is the number of times `s[i + 1] == '*'` was encountered.
    #   - `ans` will contain up to `k` alphabetic characters from `s`, possibly including every second character if `s[i + 1] == '*'`.
    #
    #### Conclusion
    #
    #After the loop has executed all possible iterations, the final output state will be:
    #
    #- `s`: The input string.
    #- `k`: The initial value, which remains constant.
    #- `ans`: A list containing up to `k` alphabetic characters from `s`, possibly including every second character if `s[i + 1] == '*'` was encountered multiple times.
    #- `i`: The final value of `i` will be the smallest value between `len(s)` and `k + 2 * n` where `n` is the number of times `s[i + 1] == '*'` was encountered.
    #
    #**Output State:**
    #- `s`: The input string.
    #- `k`: The initial value of `k`.
    #- `ans`: A list of up to `k` alphabetic characters from `s`, possibly including every second character if `s[i + 1] == '*'` was encountered.
    #- `i`: The smallest value between `len(s)` and `k + 2 * n` where `n` is the number of times `s[i + 1] == '*'` was encountered.
    if (len(ans) == k) :
        print(''.join(ans))
    else :
        print('Impossible')
    #State of the program after the if-else block has been executed: *`s` is the input string, `k` is the initial value, `ans` is a list of up to `k` alphabetic characters from `s`, possibly including every second character if `s[i + 1] == '*'` was encountered, and `i` is the smallest value between `len(s)` and `k + 2 * n` where `n` is the number of times `s[i + 1] == '*'` was encountered. If the length of `ans` is exactly `k`, then `ans` is printed. Otherwise, the message 'Impossible' is printed.
#Overall this is what the function does:The function `func` accepts a string `s` consisting only of lowercase Latin letters, «*», and «?», and an integer \( k \) such that \( 1 \leq k \leq 200 \). It processes the string `s` to construct a list `ans` containing up to `k` alphabetic characters from `s`. Specifically, it appends each alphabetic character to `ans` and includes every second character following a `'*'` symbol. If the constructed list `ans` contains exactly `k` alphabetic characters, it prints the list as a string. Otherwise, it prints 'Impossible'.

