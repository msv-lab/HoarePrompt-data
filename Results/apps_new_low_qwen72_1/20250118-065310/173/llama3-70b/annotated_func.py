#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, a is a list of n integers where 1 ≤ a_i ≤ 5, and b is a list of n integers where 1 ≤ b_i ≤ 5.
def func():
    n = int(input())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

count_a = [0] * 6

count_b = [0] * 6
    for i in a:
        count_a[i] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 100\), `a` is a list of \(n\) integers where each integer \(a_i\) satisfies \(1 \leq a_i \leq 5\), `b` is a list of \(n\) integers where each integer \(b_i\) satisfies \(1 \leq b_i \leq 5\), `count_a` is updated to reflect the frequency of each integer in `a`, `count_b` is `[0, 0, 0, 0, 0, 0]`.
    for i in b:
        count_b[i] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 100\), `a` is a list of \(n\) integers where each integer \(a_i\) satisfies \(1 \leq a_i \leq 5\), `b` is a list of \(n\) integers where each integer \(b_i\) satisfies \(1 \leq b_i \leq 5\), `count_a` is updated to reflect the frequency of each integer in `a`, `count_b` is a list where each index \(i\) (1 through 5) reflects the frequency of integer \(i\) in `b`. The loop will execute exactly `n` times if `b` contains `n` elements, updating `count_b` accordingly. If `b` is empty, the loop will not execute and `count_b` will remain `[0, 0, 0, 0, 0, 0]`.
    ans = 0
    for i in range(1, 6):
        ans += abs(count_a[i] - count_b[i])
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 100\), `a` is a list of \(n\) integers where each integer \(a_i\) satisfies \(1 \leq a_i \leq 5\), `b` is a list of \(n\) integers where each integer \(b_i\) satisfies \(1 \leq b_i \leq 5\), `count_a` is updated to reflect the frequency of each integer in `a`, `count_b` is a list where each index \(i\) (1 through 5) reflects the frequency of integer \(i\) in `b`, `ans` is `abs(count_a[1] - count_b[1]) + abs(count_a[2] - count_b[2]) + abs(count_a[3] - count_b[3]) + abs(count_a[4] - count_b[4]) + abs(count_a[5] - count_b[5])`.
    print(ans // 2)
#Overall this is what the function does:The function reads an integer `n` and two lists `a` and `b` of `n` integers each, where each integer is between 1 and 5. It then calculates the total number of changes required to make the frequency of each integer in `a` match the frequency of the same integer in `b`. This is done by computing the sum of the absolute differences between the frequencies of each integer in `a` and `b`, and then dividing the result by 2. The function prints this value. The function assumes that `n` is within the valid range (1 ≤ n ≤ 100) and that both `a` and `b` contain exactly `n` integers. If the input lists are not of the expected length or contain invalid integers, the function's behavior is undefined.

