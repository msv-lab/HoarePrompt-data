#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, X is an integer such that 2 ≤ X ≤ 10^18.
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
        #The program returns None
    #State: `mx` is 0, `t` is a positive integer such that 1 ≤ t ≤ 1000, `x` is an input integer, `subseq_lens` is an empty list, and `x` is not equal to 2
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
        
    #State: Output State: `mx` is the maximum value found among the values appended to `subseq_lens`, `t` is a positive integer such that 1 ≤ `t` ≤ 1000, `x` is 0, `subseq_lens` is a list containing all the values of `i - 1` found during each iteration of the loop until `x` becomes 0, and `i` is the highest power of 2 that is less than or equal to the current value of `x` at the start of each iteration.
    #
    #In simpler terms, `mx` will hold the maximum length of the subsequence found during the loop's iterations, `x` will be reduced to 0 after all iterations, `subseq_lens` will contain a list of lengths of subsequences found, and `i` will be the highest power of 2 that fits into the current value of `x` at the beginning of each iteration.
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: Output State: `mx` is the maximum value found among the values appended to `subseq_lens`, `t` is a positive integer such that \(1 \leq t \leq 1000\), `x` is 0, `subseq_lens` is a list containing all the values of `i - 1` found during each iteration of the loop until `x` becomes 0, `i` is `len(subseq_lens) + 1`, `len(subseq_lens)` is at least 4, and `ansv` is a list that now contains three additional elements which are `subseq_lens[1]`, `subseq_lens[2]`, and `subseq_lens[3]`.
    #
    #This means that after the loop has executed all its iterations, `subseq_lens` will contain at least four elements (since it starts with at least two elements and the loop appends one more element per iteration). The variable `ansv` will have been updated to include the last three elements that were appended to `subseq_lens` during the loop's iterations. The variable `i` will be set to the length of `subseq_lens` plus one, indicating that the loop has completed its execution. The value of `mx` will be the highest value found in `subseq_lens`, and `t` remains within the specified range.
    print(len(ansv))
    #This is printed: 3
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: `i` is 3, `ansv` contains at least 7 elements, `mx` is the maximum value found among the values in `subseq_lens`, `t` is a positive integer such that \(1 \leq t \leq 1000\), `x` is 0, `subseq_lens` contains at least 7 elements, and `ansv` includes the last three elements appended to `subseq_lens` during the loop's iterations.
    print()
    #This is printed: Output:
#Overall this is what the function does:The function reads an integer input `x` and processes it to find the maximum length of a subsequence where each element is a power of 2. It then constructs a list `ansv` based on this maximum length and prints the length of `ansv` followed by its elements. The function ultimately returns `None`.

