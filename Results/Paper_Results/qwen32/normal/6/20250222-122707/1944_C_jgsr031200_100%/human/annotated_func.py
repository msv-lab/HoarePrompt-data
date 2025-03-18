#State of the program right berfore the function call: arr is a list of integers where each integer a_i satisfies 0 <= a_i < n, and the length of arr is n, where n is an integer such that 1 <= n <= 2 * 10^5. The function is called once for each test case, and the sum of n over all test cases does not exceed 2 * 10^5.
def func_1(arr):
    freq = [0] * (n + 1)
    for i in arr:
        freq[i] += 1
        
    #State: `freq` is a list where each index `i` from 0 to n (inclusive) holds the count of how many times the integer `i` appears in the list `arr`.
    cou = 0
    for i in range(n + 1):
        if freq[i] >= 2:
            continue
        
        if freq[i] == 1:
            cou += 1
        
        if cou == 2 or freq[i] == 0:
            print(i)
            break
        
    #State: The loop prints the first index `i` where `freq[i]` is 0 or the second index `i` where `freq[i]` is 1, whichever comes first, and then terminates.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` where each integer is between 0 and n-1, and the length of the list is n. It prints the first index `i` where the count of `i` in `arr` is 0 or the second index `i` where the count of `i` in `arr` is 1, whichever comes first.

