#State of the program right berfore the function call: **
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = map(int, raw_input().split())
    ans = 0
    for i in range(n - 2, -1, -1):
        if c[i] != c[i + 1]:
            ans = i + 1
            break
        
    #State of the program after the  for loop has been executed: `ans` is the index of the first occurrence where `c[i]` is not equal to `c[i + 1]`, `n` is greater than or equal to 2. If no such occurrence is found, `ans` remains 0.
    print(ans)
#Overall this is what the function does:The function reads input from the user, processes it to find the index of the first occurrence where consecutive elements in the list `c` are different, and prints this index. If no such occurrence is found, it prints 0. The function does not accept any parameters and always outputs the index or 0 based on the processed input.

