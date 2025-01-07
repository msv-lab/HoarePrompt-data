#State of the program right berfore the function call: n and k are integers such that 1 ≤ n, k ≤ 10^18.
def func():
    n, k = map(int, input().split())
    seen = set()
    for i in range(1, k + 1):
        remainder = n % i
        
        if remainder in seen:
            print('No')
            exit()
        
        seen.add(remainder)
        
    #State of the program after the  for loop has been executed: `n` is an input integer such that 1 ≤ `n` ≤ 10^18; `k` is an input integer such that `k` is greater than or equal to 1; `seen` contains all unique remainders of `n` modulo `i` for `i` from 1 to `k`.
    print('Yes')
#Overall this is what the function does:The function accepts two integers `n` and `k` from user input, where both are between 1 and 10^18. It computes the unique remainders of `n` when divided by each integer from 1 to `k`. If any remainder is repeated during this process, the function outputs 'No' and exits. If all remainders are unique, it outputs 'Yes'. The function does not have any return value as it only prints the result directly.

