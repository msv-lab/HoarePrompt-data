#State of the program right berfore the function call: n is an integer such that 1 <= n <= 2*10^5, p is a list of integers where each element p_i is an integer such that 1 <= p_i <= n, and b is a list of integers consisting of zeros and ones, where the length of p and b is equal to n.
def func():
    n = int(input())
    p = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if p[i] != i + 1:
            ans += 1
        
        if b[i] == 0:
            ans += 1
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `p` is a list of input integers, `b` is a list of input integers, `ans` is the sum of the number of times `p[i]` is not equal to `i + 1` and the number of times `b[i]` is 0 for all `i` in the range of `n`.
    print(ans)
#Overall this is what the function does:The function takes no parameters but reads three inputs from the user: an integer `n` and two lists of integers `p` and `b` of length `n`. It calculates and returns the total count of two types of mismatches: the number of elements in `p` that do not match their 1-indexed position (`p[i]!= i + 1`) and the number of zeros in the list `b`. The final state of the program is that it prints this total count to the console, effectively providing a measure of discrepancy between the list `p` and the expected sequence, as well as the prevalence of zeros in the list `b`.

