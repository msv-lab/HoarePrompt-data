#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ n ≤ 100 and 1 ≤ k ≤ 100, and marks is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ k.
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
        
    #State of the program after the loop has been executed: Output State:
#Overall this is what the function does:The function accepts two positive integers `n` and `k`, and a list of `n` integers `marks` where each integer in `marks` is between 1 and `k`. It calculates the minimum number of additional integers, each equal to `k`, needed to be added to `marks` such that the average of the resulting list (including these additional integers) is at least `k`. If the initial average of `marks` is already at least `k`, it returns 0. The function prints and returns the number of additional integers needed.

