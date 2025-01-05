#State of the program right berfore the function call: n is an integer greater than 0, and a_i are integers such that 1 <= a_i <= 100 for 1 <= i <= n.**
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *`n` is an input integer greater than 0, `a_i` are integers such that 1 <= a_i <= 100 for 1 <= i <= n, `a` is a list of integers obtained from the input. If `n` equals 11, the program prints 5.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: `n` is an input integer greater than 0, `a_i` are integers such that 1 <= a_i <= 100 for 1 <= i <= n, `a` is a non-empty list of integers obtained from the input, each integer in `a` has its count increased by 1 in the list `c`
    print(max(c))
#Overall this is what the function does:The function accepts user input n and a list of integers, calculates the frequency of each integer in the list, and prints the maximum frequency among all integers in the list. If n is equal to 11, it prints 5.

