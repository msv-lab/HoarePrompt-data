#State of the program right berfore the function call: arr is a list of integers where each integer \( a_i \) satisfies \( 0 \le a_i < n \), and \( n \) is the length of the list \( arr \).
def func_1(arr):
    freq = [0] * (n + 1)
    for i in arr:
        freq[i] += 1
        
    #State: `freq` is a list where each element at index \( i \) represents the number of times the integer \( i \) appears in the list `arr`. The length of `freq` remains \( n + 1 \), and the elements at indices that do not correspond to any integer in `arr` remain 0.
    cou = 0
    for i in range(n + 1):
        if freq[i] >= 2:
            continue
        
        if freq[i] == 1:
            cou += 1
        
        if cou == 2 or freq[i] == 0:
            print(i)
            break
        
    #State: The loop prints the first index \( i \) where either `cou` reaches 2 or `freq[i]` is 0, and `cou` will be either 0, 1, or 2.
#Overall this is what the function does:The function `func_1` takes a list of integers `arr` where each integer is between 0 and the length of the list minus one, inclusive. It does not return a value. Instead, it prints the first index \( i \) where either the count of unique integers in `arr` reaches 2 or the frequency of the integer \( i \) is 0. If the loop completes without finding such an index, no output is produced.

