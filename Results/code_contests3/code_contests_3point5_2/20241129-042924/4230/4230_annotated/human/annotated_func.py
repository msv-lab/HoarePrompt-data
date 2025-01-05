#State of the program right berfore the function call: n is an integer such that 2 <= n <= 200000. The sequence of n integers consists of 0s and 1s representing the doors opened by Mr. Black, where 0 indicates a door in the left exit and 1 indicates a door in the right exit.**
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = map(int, raw_input().split())
    ans = 0
    for i in range(n - 2, -1, -1):
        if c[i] != c[i + 1]:
            ans = i + 1
            break
        
    #State of the program after the  for loop has been executed: `n` is the first integer element of the door sequence list, `ans` is the index of the last element in the list where the element changes, `n` is greater than or equal to 2, `c` is a list.
    print(ans)
#Overall this is what the function does:The function `func` reads a sequence of integers representing the doors opened by Mr. Black. It then iterates through the sequence and determines the index of the last element where the door changes from left to right exit or vice versa. The function prints this index as the final output.

