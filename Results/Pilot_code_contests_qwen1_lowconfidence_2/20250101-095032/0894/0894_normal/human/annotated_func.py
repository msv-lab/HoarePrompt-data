#State of the program right berfore the function call: N and L are integers such that 1 ≤ N, L ≤ 100. S_1, S_2, ..., S_N are strings of length L consisting of lowercase letters.
def func():
    n, l = map(int, raw_input().split())
    s = [raw_input() for _ in xrange(n)]
    s.sort()
    ans = ''
    for i in xrange(n):
        ans += s[i]
        
    #State of the program after the  for loop has been executed: `n` must be greater than 0, `l` is an integer between 1 and 100, `s` is a list of `n` strings sorted in lexicographical order, each string of length `l` consisting of lowercase letters, `ans` is the concatenation of all strings in the list `s`.
    print(ans)
#Overall this is what the function does:The function `func()` accepts two integers `N` and `L` (with \(1 \leq N, L \leq 100\)) and a list of `N` strings, each of length `L` consisting of lowercase letters. It sorts the list of strings in lexicographical order and then concatenates all the strings in the sorted list to form a single string `ans`. Finally, it prints the concatenated string `ans`. If `N` is zero or any of the constraints are not met, the function still reads the inputs but does not perform the sorting and concatenation steps, resulting in no output.

