#State of the program right berfore the function call: n and k are integers such that 1 ≤ n, k ≤ 10^18.**
def func():
    n, k = map(int, input().split())
    seen = set()
    for i in range(1, k + 1):
        remainder = n % i
        
        if remainder in seen:
            print('No')
            exit()
        
        seen.add(remainder)
        
    #State of the program after the  for loop has been executed: After the loop finishes executing, `n` and `k` are integers such that 1 ≤ n, k ≤ 10^18. `i` is k. `seen` is a set containing all unique remainders from the division of n by each i from 1 to k. If any remainder is repeated in `seen`, the function has printed 'No' at some point during the loop execution.
    print('Yes')
#Overall this is what the function does:The function `func` reads two integers `n` and `k` from input, calculates the remainder of `n` divided by each integer from 1 to `k`, and checks if any remainder is repeated. If a repeated remainder is found, it prints 'No' and exits the program. Otherwise, it prints 'Yes'. The function lacks a clear return value and seems to be incomplete as it does not explicitly return any value.

