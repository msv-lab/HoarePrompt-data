#State of the program right berfore the function call: arr is a list of integers where 0 <= arr[i] < len(arr) for all 0 <= i < len(arr).
def func_1(arr):
    freq = [0] * (n + 1)
    for i in arr:
        freq[i] += 1
        
    #State: `freq` is a list where each element at index `i` represents the number of times the integer `i` appears in the list `arr`. The length of `freq` remains `n + 1`.
    cou = 0
    for i in range(n + 1):
        if freq[i] >= 2:
            continue
        
        if freq[i] == 1:
            cou += 1
        
        if cou == 2 or freq[i] == 0:
            print(i)
            break
        
    #State: `cou` is 0 or 1, and the loop prints the first integer `i` where `freq[i] == 0` or the second integer `i` where `freq[i] == 1`. If no such integer is found, the loop completes without printing anything.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` where each element is between 0 and the length of the list (exclusive). It does not return a new list but instead prints the first integer `i` that either does not appear in `arr` or is the second unique integer in `arr` that appears exactly once. If no such integer is found, the function completes without printing anything.

