#State of the program right berfore the function call: t is an integer where 1 <= t <= 10^4, n is an integer where 1 <= n <= 2 \cdot 10^5, and a is a list of n integers where 0 <= a_i < n. The sum of n over all test cases does not exceed 2 \cdot 10^5, and for each trace a, there exists a suitable string s consisting of lowercase Latin letters a-z.
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
        
    #State: t is an integer where 1 <= t <= 10^4, n is an integer where 1 <= n <= 2 \cdot 10^5, and a is a list of n integers where 0 <= a_i < n. The sum of n over all test cases does not exceed 2 \cdot 10^5, and for each trace a, there exists a suitable string s consisting of lowercase Latin letters a-z. The loop has processed t test cases, and for each test case, it has printed a string ans constructed from the array of integers. The variable s for each test case is a list of l integers, where each integer has been incremented by the number of times the corresponding index was accessed in the array.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `l` and a list of integers `array`. It then constructs a string `ans` by mapping each integer in `array` to a corresponding lowercase letter based on a counter `s`. The counter `s` is incremented each time an index is accessed. The function prints the constructed string `ans` for each test case. The function does not return any value. After the function concludes, `t` test cases have been processed, and `t` strings have been printed, each corresponding to a test case. The variables `t`, `n`, and `a` remain unchanged, and the internal state variables `s` and `ans` are reset for each test case.

