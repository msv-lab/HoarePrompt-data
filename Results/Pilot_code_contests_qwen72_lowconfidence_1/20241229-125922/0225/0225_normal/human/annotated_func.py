#State of the program right berfore the function call: n is an integer where 1 ≤ n ≤ 3000, and the input consists of n lines, each containing a string namei and an integer ai, where namei is a non-empty string of lowercase Latin letters of length up to 10, and 0 ≤ ai ≤ n - 1. All names are distinct.
def func():
    rstrs = lambda : [str(x) for x in stdin.readline().split()]
    n = int(input())
    s, ans = sorted([rstrs() for _ in range(n)], key=lambda x: int(x[1])), []
    for i in range(n):
        if int(s[i][1]) > i:
            print(-1)
            exit()
        
        ans.insert(int(s[i][1]), ' '.join([s[i][0], str(n)]))
        
        n -= 1
        
    #State of the program after the  for loop has been executed: `n` is 0, `s` is a list of lists, each containing a string and an integer, sorted by the integer part, `ans` contains the strings `' '.join([s[i][0], str(n_original - i)])` inserted at positions `int(s[i][1])` for all `i` from 0 to `n_original - 1`, where `n_original` is the original value of `n`.
    print('\n'.join(ans))
#Overall this is what the function does:The function reads input from standard input, consisting of an integer `n` followed by `n` lines, each containing a string `namei` and an integer `ai`. It processes these inputs to generate a list of strings, ensuring that each string is placed at a specific position based on the value of `ai`. If any `ai` is greater than its index in the sorted list, the function prints `-1` and exits immediately. Otherwise, it constructs the final list by inserting each string at the specified position and then prints the list, one string per line. The function does not return any value; instead, it prints the results directly. The final state of the program after the function concludes is that `n` is reduced to 0, `s` is a sorted list of input pairs, and `ans` contains the processed strings in the correct order.

