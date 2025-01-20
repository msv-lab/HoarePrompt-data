#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 100 and 1 ≤ k ≤ 100, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ k.
def func():
    n, k = map(int, input().split())

marks = list(map(int, input().split()))

current_sum = sum(marks)

current_count = n
    while True:
        current_average = current_sum / current_count
        
        if math.ceil(current_average) >= k:
            print(current_count - n)
            break
        
        current_sum += k
        
        current_count += 1
        
    #State of the program after the loop has been executed: current\_sum = S + t \cdot k, current\_count = n + t, n, k
#Overall this is what the function does:The function `func` accepts no explicit parameters but reads two integers `n` and `k` from standard input, where `1 ≤ n ≤ 100` and `1 ≤ k ≤ 100`. It also reads a list `marks` of `n` integers, each satisfying `1 ≤ a_i ≤ k`. The function calculates the minimum number of additional integers (each equal to `k`) that need to be added to the list so that the average of the combined list becomes at least `k`. If such a combination cannot be achieved, the function returns `-1`.

