#State of the program right berfore the function call: N and L are positive integers such that 1 ≤ N, L ≤ 100. Each S_i is a string of length L consisting of lowercase letters.
def func():
    n, l = map(int, raw_input().split())
    s = [raw_input() for _ in xrange(n)]
    s.sort()
    ans = ''
    for i in xrange(n):
        ans += s[i]
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `l` is an integer provided by the user, `s` is a list of `n` strings provided by the user and sorted in ascending order, `ans` is a string containing all elements of `s` concatenated together.
    print(ans)
#Overall this is what the function does:The function reads two integers `n` and `l` from standard input, where `n` represents the number of strings and `l` is a parameter related to the strings' length. It then reads `n` strings of length `l` each and stores them in a list `s`. After sorting the list `s` in ascending order, the function concatenates all strings in the list into a single string `ans`. Finally, the function prints the concatenated string `ans`. Potential edge cases include when `n` or `l` are out of the specified range (1 to 100). If the input does not conform to these constraints, the behavior is undefined. Missing functionality is that the function does not validate the input `n` and `l` to ensure they are within the specified range.

