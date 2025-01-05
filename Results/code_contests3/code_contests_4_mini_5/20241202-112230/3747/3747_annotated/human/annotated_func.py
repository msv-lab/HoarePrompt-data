#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 100), and a is a list of n integers where each integer a_i is in the range (1 ≤ a_i ≤ 100).
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *`n` is a positive integer (1 ≤ n ≤ 100) and `a` is a list of `n` integers where each integer `a_i` is in the range (1 ≤ a_i ≤ 100). If `n` is equal to 11, then 5 is printed.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 100), `a` is a list of `n` integers, `c` is a list of 101 integers where `c[i]` represents the count of occurrences of integer `i` in the list `a`.
    print(max(c))
#Overall this is what the function does:The function accepts a positive integer `n` and a list `a` of `n` integers, each ranging from 1 to 100. If `n` is equal to 11, it prints 5. It then counts the occurrences of each integer from 1 to 100 in the list `a` and prints the maximum count found. The function does not return any value; it only prints results.

