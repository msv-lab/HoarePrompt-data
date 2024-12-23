#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 500, and s is a string of length n consisting of lowercase Latin letters.
def func():
    n = int(input())
    s = input()
    ans = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `i` is `n`, `n` is the same as the initial value, `s` is the same as the initial value, `ans` is the count of distinct consecutive pairs in the string `s` (ranging from 1 to `n-1`).
    print(ans)
#Overall this is what the function does:The function reads an integer \( n \) and a string \( s \) of length \( n \) as input. It then iterates through the string \( s \) to count the number of distinct consecutive pairs of characters. The function prints the count of these distinct pairs. If two consecutive characters in the string are different, the count \( ans \) is incremented. The function does not accept any parameters and returns no value; instead, it performs the counting operation internally and prints the result. Potential edge cases include when the string \( s \) consists of all the same characters, resulting in a count of 0, or when \( s \) is empty, in which case the function will print 0 since there are no pairs to compare.

