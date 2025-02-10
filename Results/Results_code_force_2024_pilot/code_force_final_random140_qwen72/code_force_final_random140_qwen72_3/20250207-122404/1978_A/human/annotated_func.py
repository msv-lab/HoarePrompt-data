#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 500, representing the number of test cases. For each test case, n is an integer where 2 ≤ n ≤ 100, representing the number of books. a is a list of n integers where 1 ≤ a_i ≤ 10^9, representing the number of pages in each book.
def func():
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        
        ls = input().split()
        
        last = int(ls.pop())
        
        other = int(sorted(ls).pop())
        
        print(last + other)
        
    #State: `t` is an integer between 1 and 500 (inclusive), `i` is `t-1`, `n` is an input integer where 2 ≤ n ≤ 100, `a` is a list of n integers where 1 ≤ a_i ≤ 10^9, `ls` is a list of strings obtained from the input with one element removed, `last` is the integer value of the last element removed from `ls`, `other` is the integer value of the largest element in the sorted `ls`.
#Overall this is what the function does:The function reads multiple test cases from the standard input. For each test case, it reads the number of books and their page counts, then calculates and prints the sum of the last page count and the second-largest page count from the input list. After processing all test cases, the function completes without returning any value.

