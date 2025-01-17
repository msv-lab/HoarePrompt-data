#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 5000, and for each test case, n is a positive integer such that 1 ≤ n ≤ 50, and the list contains 2n positive integers where each integer is in the range 1 ≤ a_i ≤ 10^7.
def func():
    t = int(input())
    ans_f = []
    for i in range(t):
        ans = 0
        
        n = int(input())
        
        l = input()
        
        lst = l.split(' ')
        
        for i in range(n * 2):
            if len(lst) != 2:
                ans += min(int(lst[0]), int(lst[1]))
                lst.remove(lst[0 * 2])
                lst.remove(lst[1 * 2])
            else:
                ans += min(int(lst[0]), int(lst[1]))
                break
        
        ans_f.append(ans)
        
    #State of the program after the  for loop has been executed: `t` is a positive integer such that \(1 \leq t \leq 5000\), `n` is a non-negative integer (the value of `n` changes with each iteration), `ans_f` is a list containing the sums of the minimum values of the pairs of elements from `lst` for each of the `t` iterations, and `i` is `n * 2` (the value of `i` is dependent on the current value of `n`).
    for i in ans_f:
        print(i)
        
    #State of the program after the  for loop has been executed: `t` is a positive integer such that \(1 \leq t \leq 5000\), `n` is a non-negative integer, `ans_f` is an empty list, and `i` is no longer relevant (since the loop has finished).
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of a positive integer \( n \) and a list of \( 2n \) positive integers. For each test case, it calculates the sum of the minimum values of all possible pairs of elements from the list and stores these sums in a list. After processing all test cases, it prints each sum in the list. The function handles up to 5000 test cases, with \( n \) ranging from 1 to 50 and each element in the list ranging from 1 to \( 10^7 \).

