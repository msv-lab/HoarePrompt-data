#State of the program right berfore the function call: n is an integer such that 2 <= n <= 200,000. The sequence of opened doors is a list of n integers where each integer is either 0 or 1.**
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = map(int, raw_input().split())
    ans = 0
    for i in range(n - 2, -1, -1):
        if c[i] != c[i + 1]:
            ans = i + 1
            break
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 <= n <= 200,000, the sequence of opened doors is a list of n integers, `c` is a list of integers obtained from input. If there exists at least one pair of consecutive elements in `c` that are different, then `ans` is the index of the first differing pair of elements. If all consecutive elements in `c` are the same, then `ans` remains 0.
    print(ans)
#Overall this is what the function does:The function does not accept any parameters. It reads input to determine the number of doors and their initial state. Then, it iterates through the sequence of door states and finds the first index where consecutive door states differ. The function prints the index of the first differing pair of elements. If all consecutive elements in the sequence are the same, it prints 0.

