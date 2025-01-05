#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 200000, and the sequence of opened doors is a list of integers where each integer is either 0 (indicating a door in the left exit) or 1 (indicating a door in the right exit), with at least one 0 and one 1 in the sequence.
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = map(int, raw_input().split())
    ans = 0
    for i in range(n - 2, -1, -1):
        if c[i] != c[i + 1]:
            ans = i + 1
            break
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `ans` is the index of the first differing element from the end, or `0` if all elements are equal or if the loop does not execute.
    print(ans)
#Overall this is what the function does:The function accepts an integer `n` and a list `c` of integers (0s and 1s) representing opened doors. It checks for the first index from the end where the door type changes (from 0 to 1 or from 1 to 0). If such a differing element exists, it returns the index of that element plus one; otherwise, it returns 0 if all elements are equal or if there are no differing elements.

