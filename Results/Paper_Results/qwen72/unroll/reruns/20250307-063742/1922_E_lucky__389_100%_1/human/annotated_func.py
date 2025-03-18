#State of the program right berfore the function call: The function should take an integer X (2 \le X \le 10^{18}) as input, and the input should be provided through multiple test cases, where the number of test cases t is an integer (1 \le t \le 1000).
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
        #The program returns nothing.
    #State: The function should take an integer X (2 ≤ X ≤ 10^18) as input, and the input should be provided through multiple test cases, where the number of test cases t is an integer (1 ≤ t ≤ 1000). `x` is assigned the value of the input integer. `subseq_lens` is an empty list. `mx` is 0. Additionally, `x` is not equal to 2.
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
        
    #State: x = 0, subseq_lens is a list of integers representing the lengths of the subsequences of powers of 2 that sum up to the initial value of x, and mx is the maximum length of these subsequences.
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: x is 0, subseq_lens is a list of integers representing the lengths of the subsequences of powers of 2 that sum up to 0, mx is the maximum length of these subsequences, ansv is a list containing the integers from 0 to mx-1 followed by the elements of subseq_lens from index 1 to the end.
    print(len(ansv))
    #This is printed: - The `print(len(ansv))` statement will print the total length of the `ansv` list.
    #
    #Output:
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: x is 0, subseq_lens is a list of integers representing the lengths of the subsequences of powers of 2 that sum up to 0, mx is the maximum length of these subsequences, ansv is a list containing the integers from 0 to mx-1 followed by the elements of subseq_lens from index 1 to the end.
    print()
    #This is printed: (newline character)
#Overall this is what the function does:The function `func_1` reads an integer `x` from the user input, where `2 ≤ x ≤ 10^18`. If `x` is 2, it prints "1" and "0" and then returns without further processing. For other values of `x`, it calculates the lengths of the subsequences of powers of 2 that sum up to `x`, and stores these lengths in a list `subseq_lens`. It then constructs a list `ansv` that contains integers from 0 to the maximum length of these subsequences minus 1, followed by the elements of `subseq_lens` from index 1 to the end. The function prints the length of `ansv` and then prints the elements of `ansv` separated by spaces, followed by a newline. The function does not accept any parameters and does not return any value.

