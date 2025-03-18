#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, X is an integer such that 2 ≤ X ≤ 10^{18}.
def func_1():
    x = int(input())
    subseq_lens = []
    mx = 0
    if (x == 2) :
        print(1)
        #This is printed: 1
        print(0)
        #This is printed: 0
        return
        #The program does not return any value since there is no return statement in the provided code.
    #State: `mx` is 0, `t` is a positive integer such that 1 ≤ t ≤ 1000, `x` is an integer such that 2 ≤ X ≤ 10^18, and `subseq_lens` is an empty list. The value of `x` is not 2
    while x != 0:
        i = 0
        
        while 2 ** i <= x:
            i += 1
        
        if i == 0:
            break
        else:
            subseq_lens.append(i - 1)
            x -= 2 ** (i - 1)
            mx = max(mx, i - 1)
        
    #State: Output State: `mx` is 10, `t` is a positive integer such that 1 ≤ t ≤ 1000, `x` is 0, `subseq_lens` is a list containing the values [5, 10, 9], and `i` is 0.
    #
    #Explanation: After the first three iterations, we know that `subseq_lens` has been updated with the values 5, 10, and 9, and `mx` has been updated to 10. Since `x` is reduced to 0 after each iteration and the loop condition `x != 0` is no longer satisfied, the loop will terminate. Therefore, after all iterations, `x` will be 0, `subseq_lens` will contain the values [5, 10, 9], `mx` will be 10, and `i` will be 0 as the inner while loop will exit when `2 ** i > x`.
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: Output State: `mx` is 10, `t` is a positive integer such that 1 ≤ t ≤ 1000, `x` is 0, `subseq_lens` is a list containing the values [5, 10, 9], `i` is 2, `ansv` is a list containing the values [0, 1, 2, 3, 4, 5, 5, 9].
    #
    #Explanation: The loop iterates from `i = 1` to `i = len(subseq_lens) - 1`, which means it will run for a total of 2 iterations based on the given `subseq_lens` list (since `len(subseq_lens)` is 3, but the loop starts from 1). After 3 iterations as shown in the provided states, `i` is 2, indicating the loop has completed its execution. Therefore, `ansv` will contain the appended values from `subseq_lens` starting from index 1 to the end, which are [5, 5, 9]. The other variables (`mx`, `t`, `x`) remain unchanged as they are not affected by the loop.
    print(len(ansv))
    #This is printed: 8
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: `i` is 4, `ansv` is a list containing the values [0, 1, 2, 3, 4, 5, 5, 9, 5, 9].
    print()
    #This is printed: an empty line
#Overall this is what the function does:The function reads an integer `x` from the user. It then calculates a sequence of integers and stores them in a list `subseq_lens`. It also determines the maximum value in this list and stores it in `mx`. After processing, it constructs a new list `ansv` based on `mx` and `subseq_lens`, and prints the length of `ansv` followed by its elements. The function does not return any value.

