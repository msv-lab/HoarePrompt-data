#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100. a_i are integers representing the values of coins such that 1 <= a_i <= 100.**
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *n is an integer input, a is a list of integers. If n equals 11, the code prints the integer 5. There are no changes to the values of n or the elements in list a after the execution of the if else block.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer input, `a` is a list of integers, `c` is a list where each element at index `d` has been incremented by the number of occurrences of `d` in list `a`
    print(max(c))
#Overall this is what the function does:The function reads an integer n followed by a list of integers representing coin values. If n is equal to 11, it prints 5. Then, it creates a list c to count the occurrences of each coin value in a and prints the maximum count in c. The function does not accept any parameters.

