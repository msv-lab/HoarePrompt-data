#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 \cdot 10^5. It is guaranteed that for the given trace, there exists a suitable string s consisting of lowercase Latin letters a-z.
def func_1(n, a):
    s = ''
    char_count = [0] * 26
    for i in range(n):
        for j in range(26):
            if char_count[j] == a[i]:
                s += chr(j + ord('a'))
                char_count[j] += 1
                break
        
    #State: `s` contains characters based on the values in `a` in the order they are matched, and `char_count` reflects the frequency of each character added to `s`.
    return s
    #The program returns the string `s` which contains characters based on the values in `a` in the order they are matched.
#Overall this is what the function does:The function constructs and returns a string `s` consisting of lowercase Latin letters, where each character in the string corresponds to an integer in the input list `a`. The character is chosen such that the number of times it appears in the string matches the value specified by the corresponding integer in `a`.

