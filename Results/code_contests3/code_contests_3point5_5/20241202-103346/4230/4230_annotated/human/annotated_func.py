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
        
    #State of the program after the  for loop has been executed: If there exists at least one element in list `c` that is different from its adjacent element, then `ans` will be equal to the index of the first occurrence of this element in reverse order. Otherwise, `ans` will remain 0.
    print(ans)
#Overall this is what the function does:The function reads input from the user, processes it, and prints the index of the first element in a list that is different from its adjacent element in reverse order. If no such element is found, it prints 0.

