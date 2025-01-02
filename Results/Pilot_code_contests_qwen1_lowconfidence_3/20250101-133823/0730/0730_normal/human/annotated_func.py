#State of the program right berfore the function call: s is a string consisting of 'L' and 'R', where the length of s is N (1 ≤ N ≤ 10^5), and K is an integer such that 1 ≤ K ≤ 10^5.
def func_1(s):
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] == 'L' and i >= 1 and s[i - 1] == 'L':
            ans += 1
        elif s[i] == 'R' and i <= n - 2 and s[i + 1] == 'R':
            ans += 1
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of 'L' and 'R', `n` is a positive integer, `ans` is the count of consecutive pairs of 'LL' and 'RR' in the string `s`.
    return ans
    #The program returns ans which is the count of consecutive pairs of 'LL' and 'RR' in the string 's'
#Overall this is what the function does:The function `func_1` accepts a string `s` consisting of 'L' and 'R', and returns the count of consecutive pairs of 'LL' and 'RR' in the string `s`. After executing the function, the program state will have the variable `ans` containing the total count of such consecutive pairs. The function iterates through the string `s` and increments `ans` whenever it finds two consecutive 'L' characters ('LL') or two consecutive 'R' characters ('RR'). The function handles all edge cases, including when the string `s` is very short (length 1 or 2), ensuring no out-of-bounds errors occur during the iteration.

