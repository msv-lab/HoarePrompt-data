#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 200,000, and the sequence of opened doors is a list of integers where each integer is either 0 (indicating a door in the left exit) or 1 (indicating a door in the right exit), with at least one 0 and one 1 in the list.
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = map(int, raw_input().split())
    ans = 0
    for i in range(n - 2, -1, -1):
        if c[i] != c[i + 1]:
            ans = i + 1
            break
        
    #State of the program after the  for loop has been executed: If `n` is 0 or 1, `ans` is 0. If `n` is at least 2, `ans` is the last index where `c[i]` is not equal to `c[i + 1]` or remains 0 if all elements are equal.
    print(ans)
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 200,000) and a list of integers representing opened doors, where each integer is either 0 (left exit) or 1 (right exit). It identifies the last index where the door configuration changes from 0 to 1 or from 1 to 0, returning that index. If all doors are the same (either all 0s or all 1s), the function will return 0. It does not handle cases where the input may not conform to the expected format, such as non-integer values.

