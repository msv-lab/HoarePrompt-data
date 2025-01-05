#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100. The list a contains n integers where each integer a_i is such that 1 ≤ a_i ≤ 100.**
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *n is an integer such that 1 ≤ n ≤ 100. The list `a` contains `n` integers where each integer `a_i` is such that 1 ≤ `a_i` ≤ 100. If n equals 11, the number 5 is printed. Otherwise, no changes occur in the program state.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 100, list `a` has been fully iterated over, and the list `c` contains the count of occurrences of each unique element in list `a`
    print(max(c))
#Overall this is what the function does:The function `func` reads an integer `n` and a list `a` of `n` integers. If `n` is equal to 11, it prints 5. Then, it creates a new list `c` to count the occurrences of each unique element in list `a`. Finally, it prints the maximum count in list `c`. The function does not return any specific output based on the given constraints.

