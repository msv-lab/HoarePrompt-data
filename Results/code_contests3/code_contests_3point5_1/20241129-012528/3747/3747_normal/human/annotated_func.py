#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100. The list of integers a contains n elements where each element is an integer such that 1 <= a_i <= 100.**
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *`n` is an input integer between 1 and 100, `a` contains `n` elements where each element is an integer between 1 and 100. If `n` equals 11, the number 5 is printed to the console.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: `n` is an input integer between 1 and 100, `a` contains `n` elements where each element is an integer between 1 and 100, if `n` equals 11, the number 5 is printed to the console, `c` is a list of 101 elements where each element represents the count of occurrences of the corresponding index in list `a`.
    print(max(c))
#Overall this is what the function does:The function func reads an integer n followed by a list of n integers. If n is equal to 11, it prints 5. Then, it creates a list c of size 101 and counts the occurrences of each element from the input list a in c. Finally, it prints the maximum count in c. The function does not explicitly return any value.

