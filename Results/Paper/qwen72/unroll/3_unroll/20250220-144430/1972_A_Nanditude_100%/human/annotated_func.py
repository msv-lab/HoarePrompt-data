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
        
    #State: The variable `t` is decremented by the number of iterations that have been executed. The variable `n` is the last input integer value read for the number of elements in the lists. The lists `a` and `b` are the last input lists of `n` integers sorted in non-decreasing order. The variable `cnt` is the count of elements in `b` that are less than the first element in `a` for the last iteration. The variable `i` is the index of the first element in `a` that is greater than or equal to the first element in `b` for the last iteration.
#Overall this is what the function does:The function `func` reads a series of inputs from the user. It first reads an integer `t` which represents the number of test cases. For each test case, it reads another integer `n` and two lists `a` and `b` of `n` integers each, where both lists are sorted in non-decreasing order. The function then counts the number of elements in `b` that are less than the corresponding elements in `a` and prints this count for each test case. After processing all test cases, the function concludes, and the final state is that `t` has been decremented to 0, `n` holds the last input integer value for the number of elements in the lists, and `a` and `b` hold the last input lists of `n` integers. The variable `cnt` holds the count of elements in `b` that are less than the first element in `a` for the last iteration, and `i` holds the index of the first element in `a` that is greater than or equal to the first element in `b` for the last iteration.

