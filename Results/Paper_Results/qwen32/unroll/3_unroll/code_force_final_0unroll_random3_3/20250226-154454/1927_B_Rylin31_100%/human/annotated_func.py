#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 \cdot 10^5. It is guaranteed that for the given trace, there exists a suitable string s consisting of lowercase Latin letters a-z.
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
        
    #State: a series of strings `ans` for each test case, where each string is constructed by mapping the values in `array` to characters based on the count in `s`.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it constructs and prints a string of lowercase Latin letters. The string is generated based on a list of integers, mapping each integer to a corresponding letter and incrementing a count to ensure each letter is unique within the constraints of the problem.

