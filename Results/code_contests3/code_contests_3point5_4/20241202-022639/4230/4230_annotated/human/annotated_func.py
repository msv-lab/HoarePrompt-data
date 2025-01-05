#State of the program right berfore the function call: n is an integer such that 2 <= n <= 200,000, and the sequence of opened doors is a list of integers where each integer is either 0 or 1 representing the location of the door (left or right exit).
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = map(int, raw_input().split())
    ans = 0
    for i in range(n - 2, -1, -1):
        if c[i] != c[i + 1]:
            ans = i + 1
            break
        
    #State of the program after the  for loop has been executed: `n` is at least 3, `c` is a mapped list of integers from the input, `ans` is equal to the index of the first occurrence where the element at index `i` is different from the element at index `i + 1` in the list `c`.
    print(ans)
#Overall this is what the function does:The function `func` reads an integer `n` and a sequence of integers representing the status of doors in a building. It then iterates through the sequence to find the index of the first occurrence where the status of adjacent doors differs. This index is stored in the variable `ans` and printed. The function does not return any value, it only updates the state of the doors.

