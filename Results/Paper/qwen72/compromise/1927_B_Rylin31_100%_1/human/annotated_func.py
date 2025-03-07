#State of the program right berfore the function call: t is an integer where 1 \le t \le 10^4, representing the number of test cases. For each test case, n is an integer where 1 \le n \le 2 \cdot 10^5, representing the length of the lost string. a is a list of n integers where 0 \le a_i < n, representing the trace of the string. The sum of n over all test cases does not exceed 2 \cdot 10^5, and it is guaranteed that a valid string s exists for each trace.
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
        
    #State: `t` is an integer where \(1 \le t \le 10^4\), `i` is \(t-1\), `l` is the last input integer, `s` is a list of length `l` where each element is 0 except for the elements at the indices specified by the elements in `array`, which are incremented by the number of times their index appears in `array`, `array` is a list of integers provided by the user, `ans` is a string containing the characters corresponding to the ASCII values of `s[j] + 97` for each element `j` in `array`, in the order they appear in `array`.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then constructs a string `ans` by converting each element in `a` to a corresponding character based on the current state of a list `s` of length `n`, where the character is determined by the ASCII value of `s[j] + 97` for each element `j` in `a`. The list `s` is updated by incrementing the value at the index `j` for each element `j` in `a`. After processing all test cases, the function prints the constructed string `ans` for each test case. The final state of the program includes the integer `t` (number of test cases), the integer `i` (which is `t-1`), the integer `l` (the last input integer `n`), the list `s` (where each element is 0 except for the elements at the indices specified by the elements in `array`, which are incremented by the number of times their index appears in `array`), the list `array` (the last input list of integers), and the string `ans` (the last constructed string).

