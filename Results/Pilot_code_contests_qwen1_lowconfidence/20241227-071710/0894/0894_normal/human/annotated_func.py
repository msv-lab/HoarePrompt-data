#State of the program right berfore the function call: N and L are integers such that 1 ≤ N, L ≤ 100, and for each i, S_i is a string of length L consisting of lowercase letters.
def func():
    n, l = map(int, raw_input().split())
    s = [raw_input() for _ in xrange(n)]
    s.sort()
    ans = ''
    for i in xrange(n):
        ans += s[i]
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100, `i` is 100, `l` is an integer between 1 and 100, `s` is a list of `n` strings sorted in ascending order, `ans` is the concatenation of all strings in the list `s`.
    print(ans)
#Overall this is what the function does:The function processes a set of N strings, each of length L, where 1 ≤ N, L ≤ 100, and concatenates them into a single string. The function reads N and L from standard input, followed by N lines of strings. It then sorts these strings in ascending order and concatenates them into a single string `ans`. After executing the function, the final state of the program is that `ans` contains the concatenated and sorted strings, and `n` and `l` retain their original values from the input. There are no direct parameters passed to the function; instead, it reads the necessary values from standard input.

