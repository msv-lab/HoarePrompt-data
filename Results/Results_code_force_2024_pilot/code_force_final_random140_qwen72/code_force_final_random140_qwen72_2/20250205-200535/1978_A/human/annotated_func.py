#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 500, representing the number of test cases. For each test case, n is an integer where 2 ≤ n ≤ 100, representing the number of books. a is a list of n integers where 1 ≤ a_i ≤ 10^9, representing the number of pages in each book.
def func():
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        
        ls = input().split()
        
        last = int(ls.pop())
        
        other = int(sorted(ls).pop())
        
        print(last + other)
        
    #State: After the loop executes all the iterations, `t` is equal to the number of times the loop has run (which is the initial value of `t`), `i` is `t - 1`, `n` is an input integer where 2 ≤ n ≤ 100, `a` is a list of `n` integers where 1 ≤ a_i ≤ 10^9, `ls` is a list of strings from the last user input with one less element, `last` is the integer value of the last element that was removed from the last `ls`, `other` is the largest integer value from the sorted last `ls`.
#Overall this is what the function does:The function reads a series of test cases, each consisting of a number of books and a list of the number of pages in each book. For each test case, it calculates and prints the sum of the number of pages in the last book and the number of pages in the second-largest book. After processing all test cases, the function completes without returning any value. The final state includes the processed test cases being printed, and the internal variables used in the function are no longer relevant.

