#State of the program right berfore the function call: n is an integer such that 2 <= n <= 200,000. The sequence of integers representing the doors opened by Mr. Black consists of n integers where each integer is either 0 or 1.**
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = map(int, raw_input().split())
    ans = 0
    for i in range(n - 2, -1, -1):
        if c[i] != c[i + 1]:
            ans = i + 1
            break
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 <= n <= 200,000, `c` contains the mapped input values, `ans` is equal to the value of the index i + 1 where c[i] is not equal to c[i + 1], or 0 if no such index is found.
    print(ans)
#Overall this is what the function does:The function `func` reads an integer `n` followed by a sequence of integers representing the doors opened by Mr. Black. It then iterates through the sequence to find the last index where the current door state is different from the next door state. If such an index is found, it sets `ans` to that index + 1; otherwise, it sets `ans` to 0. Finally, the function prints the value of `ans`. The function handles the constraint 2 <= n <= 200,000.

