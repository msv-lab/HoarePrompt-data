#State of the program right berfore the function call: n is an integer such that 2 <= n <= 200,000. The sequence of integers representing the doors opened by Mr. Black is a list of n integers where each integer is either 0 or 1.**
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = map(int, raw_input().split())
    ans = 0
    for i in range(n - 2, -1, -1):
        if c[i] != c[i + 1]:
            ans = i + 1
            break
        
    #State of the program after the  for loop has been executed: `n` is the first element of the list representing the doors opened by Mr. Black, `c` is a list of integers converted from the input list, `ans` is the index of the first occurrence where the value changes in the list `c`. If no such occurrence exists, `ans` remains 0.
    print(ans)
#Overall this is what the function does:The function `func` reads an integer `n` and a list of integers `c` representing the doors opened by Mr. Black. It then iterates through the list `c` backwards and finds the index of the first occurrence where the value changes. If no change occurs, it sets the result `ans` to 0. The function finally prints the value of `ans`.

