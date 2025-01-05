#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 200,000. The sequence of opened doors is a list of n integers where each integer is either 0 or 1 representing the location of the door (left exit or right exit).**
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = map(int, raw_input().split())
    ans = 0
    for i in range(n - 2, -1, -1):
        if c[i] != c[i + 1]:
            ans = i + 1
            break
        
    #State of the program after the  for loop has been executed: `n` is at least 3, `i` is 0, `ans` is at least 1. If the loop completes all iterations, `ans` will be the index of the last occurrence where the element at index `i` is different from the element at index `i + 1` in the list `c`.
    print(ans)
#Overall this is what the function does:The function `func` reads input from the user to create a list of integers representing the location of doors (left or right exit). It then iterates through the list to find the index of the last occurrence where the element at index `i` is different from the element at index `i + 1`, and prints this index as the answer. The function does not accept any parameters.

