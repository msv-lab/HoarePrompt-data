#State of the program right berfore the function call: arr is a list of integers where each integer a_i satisfies 0 <= a_i < n, and the length of arr is n where 1 <= n <= 2 * 10^5. The function is called multiple times for different test cases, with the total number of elements across all test cases not exceeding 2 * 10^5.
def func_1(arr):
    freq = [0] * (n + 1)
    for i in arr:
        freq[i] += 1
        
    #State: `arr` is a list of integers where each integer `a_i` satisfies `0 <= a_i < n`, the length of `arr` is `n` where `n` is at least 1, and `freq` is a list of integers initialized to 0 with a length of `n + 1`, except each `freq[j]` reflects the number of times the integer `j` appears in `arr`.
    cou = 0
    for i in range(n + 1):
        if freq[i] >= 2:
            continue
        
        if freq[i] == 1:
            cou += 1
        
        if cou == 2 or freq[i] == 0:
            print(i)
            break
        
    #State: i is the first index where freq[i] is 0, cou is 0 or 1, and freq and arr remain unchanged.
#Overall this is what the function does:The function `func_1` accepts a list `arr` of integers where each integer `a_i` is between 0 and `n-1`, and the length of `arr` is `n`. It prints the smallest integer between 0 and `n` that appears at most once in `arr` or is missing from `arr`.

