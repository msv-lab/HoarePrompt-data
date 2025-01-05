#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 200,000, and the sequence of opened doors is a list of integers where each integer is either 0 (left exit) or 1 (right exit), with at least one 0 and one 1 in the list.
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = map(int, raw_input().split())
    ans = 0
    for i in range(n - 2, -1, -1):
        if c[i] != c[i + 1]:
            ans = i + 1
            break
        
    #State of the program after the  for loop has been executed: `n` is at least 0, `ans` is the index of the last position where `c[i]` is not equal to `c[i + 1]` or 0 if all are equal, and `i` is the last index checked in the range.
    print(ans)
#Overall this is what the function does:The function accepts an integer `n` and a list of integers representing opened doors, where each integer is either 0 (left exit) or 1 (right exit). It finds and returns the index of the last position where the door value differs from the next door value. If all doors have the same value, it returns 0. The function does not handle cases where input may not meet the specified constraints (e.g., if there are no 0s or 1s).

