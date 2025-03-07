#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 2 \cdot 10^5, and a is a list of n integers where 0 <= a_i < n. The sum of n over all test cases does not exceed 2 \cdot 10^5.
def func_1(n, a):
    s = ''
    char_count = [0] * 26
    for i in range(n):
        for j in range(26):
            if char_count[j] == a[i]:
                s += chr(j + ord('a'))
                char_count[j] += 1
                break
        
    #State: `n` is a positive integer such that 1 <= n <= 200000, `i` is `n-1`, `j` is 25, and `s` is a string that contains the characters appended during each iteration of the loop. The `char_count` list will have values that are the counts of how many times each corresponding character (from 'a' to 'z') was appended to `s` based on the values in `a`.
    return s
    #The program returns the string `s` that contains the characters appended during each iteration of the loop, based on the values in `a` and the counts in `char_count`.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and a list `a` of `n` integers, where each integer `a_i` is in the range 0 to `n-1`. It returns a string `s` that is constructed by appending characters from 'a' to 'z' based on the values in `a` and their corresponding counts in a list `char_count`. The character appended to `s` for each value `a_i` is the first character in the alphabet whose count in `char_count` matches `a_i`. After the function concludes, `s` will contain the characters appended in the order specified by the values in `a` and their counts. The `char_count` list will reflect the number of times each character from 'a' to 'z' was appended to `s`.

