#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, X is an integer such that 2 ≤ X ≤ 10^{18}.
def func_1():
    x = int(input())
    x -= 1
    subseq_lens = []
    mx = 0
    while x != 0:
        i = 0
        
        while 2 ** (i + 1) <= x + 1:
            i += 1
        
        if i == 0:
            break
        else:
            subseq_lens.append(i)
            x -= 2 ** i - 1
            mx = max(mx, i)
        
    #State: Output State: `i` is 10, `x` is 0, `t` is a positive integer such that 1 ≤ t ≤ 1000, `subseq_lens` is a list containing 10 three times, and `mx` is 10.
    #
    #Explanation: The loop continues to run as long as `x` is not equal to 0. Each iteration of the loop reduces `x` by `2^i - 1`, where `i` is the value found by the inner while loop. Since `x` starts at 1023 and decreases by 1023 in the first iteration, it becomes 0 after the first iteration. However, since the problem specifies the state after the loop executes 3 times, we can infer that `x` must be reduced further in subsequent iterations, but given the nature of the loop, once `x` reaches a point where no valid `i` can be found (i.e., `2^(i+1) > x+1`), the loop breaks. Given the constraints and the fact that `x` is reduced by the maximum possible value each time (`2^10 - 1 = 1023`), it's clear that `x` will reach 0 after the third iteration, and the loop will terminate. Therefore, after all iterations, `x` will be 0, `i` will still be 10 (as it was set in the last iteration), `subseq_lens` will contain 10 three times, and `mx` will remain 10.
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: Output State: `i` is equal to the length of `subseq_lens`, `x` is 0, `t` is a positive integer such that 1 ≤ t ≤ 1000, `subseq_lens` is a list containing 10 three times, and `mx` is 10; `ansv` is a list containing the elements of `subseq_lens` from index 1 to the length of `subseq_lens`.
    #
    #Explanation: After all iterations of the loop, `i` will be equal to the length of `subseq_lens` because the loop runs from 1 to the length of `subseq_lens` minus one. The loop appends each element of `subseq_lens` starting from the second element (index 1) to `ansv`. Therefore, `ansv` will contain all elements of `subseq_lens` from index 1 to the end of the list. The other variables (`x`, `t`, and `mx`) remain unchanged as they are not affected by the loop.
    print(len(ansv))
    #This is printed: 3
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: i is 9, x is 0, t is a positive integer such that 1 ≤ t ≤ 1000, subseq_lens is a list containing [10, 10, 10], mx is 10, ansv is a list containing [10, 10, 10, 10, 10, 10, 10, 10, 10, 10].
    print()
    #This is printed: None
#Overall this is what the function does:The function processes a single test case where `t` is a positive integer between 1 and 1000, and `X` is an integer between 2 and 10^18. It calculates a sequence of integers stored in `subseq_lens` and constructs a new list `ansv` based on these values. Finally, it prints the length of `ansv` followed by its elements. The function does not return any value but prints the results directly.

