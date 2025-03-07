#State of the program right berfore the function call: arr is a list of integers where each integer a_i satisfies 0 <= a_i < n, and the length of arr is n, with 1 <= n <= 2 * 10^5. The function is called once for each test case, and the sum of n across all test cases does not exceed 2 * 10^5.
def func_1(arr):
    freq = [0] * (n + 1)
    for i in arr:
        freq[i] += 1
        
    #State: `arr` is a list of integers where each integer `a_i` satisfies 0 <= `a_i` < `n`, and the length of `arr` is `n`, with 1 <= `n` <= 2 * 10^5; `freq` is a list where the i-th element represents the number of times the integer `i-1` appears in `arr`.
    cou = 0
    for i in range(n + 1):
        if freq[i] >= 2:
            continue
        
        if freq[i] == 1:
            cou += 1
        
        if cou == 2 or freq[i] == 0:
            print(i)
            break
        
    #State: The loop will print the first index `i` where `freq[i]` is `0` or the second index `i` where `freq[i]` is `1`. The state of `arr` and `freq` remains unchanged, and `cou` will be either `1` or `2` depending on which condition caused the loop to terminate.
    #
    #Since the exact values of `arr` and `freq` are not provided, we cannot determine a specific numerical output. However, we can describe the output state in a general form:
    #
    #Output State:
#Overall this is what the function does:The function `func_1` takes a list of integers `arr` where each integer `a_i` satisfies `0 <= a_i < n` and the length of `arr` is `n`. It prints the first index `i` where `freq[i]` is `0` or the second index `i` where `freq[i]` is `1`, where `freq` is a frequency list of the integers in `arr`.

