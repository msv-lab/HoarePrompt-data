#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 \cdot 10^5. It is guaranteed that for each test case, there exists a suitable string s consisting of lowercase Latin letters a-z.
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
        
    #State: The final output is the concatenation of all `ans` strings from each of the `t` test cases.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it constructs and prints a string of lowercase Latin letters based on a given list of integers. The string is generated such that each integer in the list specifies the position in the string where the next letter in the alphabet sequence should be placed and incremented for subsequent occurrences.

