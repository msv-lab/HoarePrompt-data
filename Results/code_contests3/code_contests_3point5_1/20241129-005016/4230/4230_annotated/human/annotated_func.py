#State of the program right berfore the function call: n is an integer such that 2 <= n <= 200,000. The sequence of opened doors is represented by n integers, where each integer is either 0 or 1.**
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = map(int, raw_input().split())
    ans = 0
    for i in range(n - 2, -1, -1):
        if c[i] != c[i + 1]:
            ans = i + 1
            break
        
    #State of the program after the  for loop has been executed: `n` is 2, `c` is a list of integers based on the input, `ans` is the index of the first occurrence where the element at that index is not equal to the element at the next index in list `c`.
    print(ans)
#Overall this is what the function does:The function `func` reads a sequence of integers representing the state of opened doors and identifies the index of the first occurrence where the state changes from one door to the next. This index is then printed as the output. The function does not accept any parameters and operates solely on the predefined sequence within the function.

