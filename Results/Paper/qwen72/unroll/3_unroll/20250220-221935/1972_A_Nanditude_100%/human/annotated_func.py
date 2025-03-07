#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 100), n is a positive integer (1 ≤ n ≤ 100), a is a list of n integers sorted in non-decreasing order (1 ≤ a_1 ≤ a_2 ≤ ... ≤ a_n ≤ 10^9), and b is a list of n integers sorted in non-decreasing order (1 ≤ b_1 ≤ b_2 ≤ ... ≤ b_n ≤ 10^9).
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        b = list(map(int, input().split()))
        
        cnt = 0
        
        i = 0
        
        for j in range(n):
            if b[j] < a[i]:
                cnt += 1
            else:
                i += 1
        
        print(cnt)
        
    #State: The variable `t` is decremented by the number of iterations the loop has executed, `n` retains its last assigned value from the last iteration, and `a` and `b` retain their last assigned lists from the last iteration. The variable `cnt` is printed for each iteration and is reset to 0 at the beginning of each new iteration. The variable `i` is reset to 0 at the beginning of each new iteration.
#Overall this is what the function does:The function `func` reads multiple sets of inputs from the user. For each set, it reads an integer `n`, followed by two lists of `n` integers each, `a` and `b`, where both lists are sorted in non-decreasing order. The function then counts how many elements in `b` are less than the first element in `a`. This count is printed for each set of inputs. After processing all sets, the variable `t` is decremented by the number of sets processed, and the final state of the program includes the last assigned values of `n`, `a`, and `b` from the last set, as well as the decremented value of `t`. The function does not return any value.

