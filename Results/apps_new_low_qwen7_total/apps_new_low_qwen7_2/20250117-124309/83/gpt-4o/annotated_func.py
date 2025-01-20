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
        
    #State of the program after the loop has been executed: n is 5, k is 3, marks is [1, 2, 3, 2, 1], current_sum is 27, current_count is 11, current_average is 2.4545454545454546
#Overall this is what the function does:The function accepts no explicit parameters but reads two integers \( n \) and \( k \) from the input, followed by a list of \( n \) integers \( a \). It then calculates the smallest number of additional elements (each equal to \( k \)) that need to be appended to the list to ensure that the average of the new list is at least \( k \). If the input values do not meet the constraints \( 1 \leq n \leq 100 \), \( 1 \leq k \leq 100 \), and \( 1 \leq a_i \leq k \), it will terminate without producing a meaningful result. If the constraints are satisfied, the function prints the number of additional elements needed and exits.

