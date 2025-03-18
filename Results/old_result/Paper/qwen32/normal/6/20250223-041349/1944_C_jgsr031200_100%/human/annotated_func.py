#State of the program right berfore the function call: arr is a list of integers where 0 <= arr[i] < len(arr) for each index i, and the length of arr (n) satisfies 1 <= n <= 2 * 10^5. The function will be called multiple times with different arrays, and the sum of all n across these calls does not exceed 2 * 10^5.
def func_1(arr):
    freq = [0] * (n + 1)
    for i in arr:
        freq[i] += 1
        
    #State: `arr` is a list of integers with `n` elements, where `0 <= arr[i] < len(arr)` for each index `i`, and `freq` is a list of `n + 1` integers where each integer at index `i` represents the count of how many times `i` appears in `arr`.
    cou = 0
    for i in range(n + 1):
        if freq[i] >= 2:
            continue
        
        if freq[i] == 1:
            cou += 1
        
        if cou == 2 or freq[i] == 0:
            print(i)
            break
        
    #State: i is n + 1, cou reflects the number of times freq[i] was exactly 1 during the iterations, and freq remains unchanged.
#Overall this is what the function does:The function `func_1` takes a list of integers `arr` as input, where each integer in the list is between 0 and the length of the list minus one, inclusive. The function prints the smallest integer that appears exactly once in the list or is missing from the list.

