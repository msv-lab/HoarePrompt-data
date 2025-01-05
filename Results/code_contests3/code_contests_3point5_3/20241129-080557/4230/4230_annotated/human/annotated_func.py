#State of the program right berfore the function call: n is an integer such that 2 <= n <= 200,000, and the sequence of opened doors is a list of n integers where each integer is either 0 or 1.**
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = map(int, raw_input().split())
    ans = 0
    for i in range(n - 2, -1, -1):
        if c[i] != c[i + 1]:
            ans = i + 1
            break
        
    #State of the program after the  for loop has been executed: `n` is at least 2, `c` contains valid integers. If there exists an index `i` such that `c[i]` is not equal to `c[i + 1]`, `ans` is set to the index `i + 1` and the loop breaks. If all elements in `c` are equal, `ans` remains 0.
    print(ans)
#Overall this is what the function does:The function `func` reads an integer `n` and a list of integers `c`. It then iterates through the list `c` in reverse order, and if it finds two consecutive elements that are not equal, it sets `ans` to the index of the first occurrence and breaks the loop. It prints the final value of `ans`, which indicates the position where the elements changed. If all elements in `c` are equal, `ans` remains 0. The function does not explicitly return a value.

