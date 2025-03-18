#State of the program right berfore the function call: arr is a list of non-negative integers where each integer \(a_i\) satisfies \(0 \le a_i < n\), and \(n\) is the length of the list.
def func_1(arr):
    freq = [0] * (n + 1)
    for i in arr:
        freq[i] += 1
        
    #State: Each element in `arr` has been processed exactly once, and `freq[i]` contains the count of how many times `i` appeared in `arr`.
    cou = 0
    for i in range(n + 1):
        if freq[i] >= 2:
            continue
        
        if freq[i] == 1:
            cou += 1
        
        if cou == 2 or freq[i] == 0:
            print(i)
            break
        
    #State: The loop will terminate when `cou` reaches 2 or when `freq[i]` becomes 0 for some `i`. After all iterations, `cou` will be 2, `i` will be the smallest index where `freq[i]` is 0 or the value of `i` just before the loop breaks due to `cou == 2`. The value of `n` must be such that the loop can iterate up to `n+1` times.
#Overall this is what the function does:The function accepts a list of non-negative integers `arr`, where each integer \(a_i\) satisfies \(0 \le a_i < n\) and \(n\) is the length of the list. It counts the frequency of each integer in the list and then iterates through these frequencies. If it finds two unique integers that appear only once, it prints the smaller one and breaks the loop. If no such pair exists, it prints the smallest integer that does not appear in the list. The function does not return anything but prints the result directly.

