#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9.
def func():
    sys.stdin = BytesIO(sys.stdin.read())
    input = lambda : sys.stdin.readline().rstrip('\r\n')
    n = int(input())
    arr = [int(x) for x in input().split(' ')]
    h = max(arr)
    res = list()
    for el in arr:
        if len(res) == 0 or res[-1] != el:
            if len(res) > 0:
                if res[-1] < el:
                    print('NO')
                    exit()
            res.append(el)
        else:
            res.pop()
        
    #State of the program after the  for loop has been executed: - If the loop exits early due to the 'NO' condition, the program terminates and the final state is that 'NO' has been printed.
    #   - If the loop completes without exiting early, `res` will contain a non-decreasing subsequence of elements from `arr`.
    #
    #Therefore, the output state of the loop after all iterations have finished is:
    #
    #Output State:
    if (len(res) > 1) :
        print('NO')
    else :
        if (len(res) == 0) :
            print('YES')
        else :
            print('NO' if res[-1] < h else 'YES')
        #State of the program after the if-else block has been executed: *The loop exits early due to the 'NO' condition, the program terminates and the final state is that 'NO' has been printed, or if the loop completes without exiting early, `res` will contain a non-decreasing subsequence of elements from `arr`. Additionally, the length of `res` is less than or equal to 1. If the length of `res` is 0, 'YES' has been printed. If the length of `res` is greater than 0, the program may have terminated with 'NO' being printed or `res` contains a valid non-decreasing subsequence.
    #State of the program after the if-else block has been executed: *If the length of `res` is greater than 1, 'NO' has been printed. If the length of `res` is 0, 'YES' has been printed. If the length of `res` is 1, the program may have terminated with 'NO' being printed, or `res` contains a valid non-decreasing subsequence of elements from `arr`.
#Overall this is what the function does:This function reads input from standard input, expecting a positive integer `n` (1 ≤ n ≤ 2 ⋅ 10^5) followed by a list of `n` integers (1 ≤ a_i ≤ 10^9). It processes the list to determine if it can be reduced to a non-decreasing subsequence of length 1 or 0. If at any point during processing, it finds that the sequence cannot be reduced to such a subsequence, it prints 'NO' and terminates the program. If the sequence can be reduced to a non-decreasing subsequence of length 1 or 0, it prints 'YES'. The final state of the program is that either 'YES' or 'NO' is printed to the standard output, and the program terminates.

