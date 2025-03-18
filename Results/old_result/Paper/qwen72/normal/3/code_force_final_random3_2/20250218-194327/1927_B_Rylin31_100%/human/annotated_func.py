#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 1 <= n <= 2 \cdot 10^5, and a is a list of n integers where 0 <= a_i < n. The sum of n over all test cases does not exceed 2 \cdot 10^5, and it is guaranteed that for each trace a, there exists a suitable string s consisting of lowercase Latin letters a-z.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is an integer such that 1 <= n <= 2 \cdot 10^5, `a` is a list of `n` integers where 0 <= a_i < n, `i` is `t - 1`, `l` is an input integer greater than or equal to 0, `s` is a list of `l` integers where each element is 0 except for the elements corresponding to the indices in `array`, which are incremented by the number of times their index appears in `array`, `array` is a list of integers read from input, `j` is the last element in `array`, `ans` is a string containing the characters corresponding to the ASCII values of `s[j] + 97` for each `j` in `array`, in the order they appear in `array`.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `l` and a list of integers `array` from the input. It then constructs a string `ans` by mapping each integer in `array` to a corresponding lowercase Latin letter, where the letter is determined by the current value in a list `s` of length `l` initialized to zeros. The value in `s` at the index specified by each integer in `array` is incremented after each mapping. The function prints the constructed string `ans` for each test case. After the function concludes, the input variables `t`, `n`, and `a` are unchanged, and the program state includes the printed strings for all test cases.

