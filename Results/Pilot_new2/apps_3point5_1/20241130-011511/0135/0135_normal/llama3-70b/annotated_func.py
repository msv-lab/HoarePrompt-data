#State of the program right berfore the function call: # Precondition
**n and k are integers such that 1 <= n, k <= 10^18.**
def func():
    n, k = map(int, input().split())
    seen = set()
    for i in range(1, k + 1):
        remainder = n % i
        
        if remainder in seen:
            print('No')
            exit()
        
        seen.add(remainder)
        
    #State of the program after the  for loop has been executed: Output State: `n` and `k` are integers in the range 1 <= n, k <= 10^18, `seen` is a set containing the remainders of n % i for all i from 1 to k, `remainder` is the remainder of n % i for i in the range of 1 to k. If any remainder is repeated, the program exits without altering the initial state.
    print('Yes')
#Overall this is what the function does:The function `func` reads two integers `n` and `k` from input, calculates the remainder of `n` divided by numbers from 1 to `k`, stores these remainders in a set `seen`, and checks if any remainder is repeated. If a repeated remainder is found, it prints 'No' and exits; otherwise, it prints 'Yes'. The function does not explicitly return a value, but it handles the input and output logic based on the remainders calculated. It ensures `n` and `k` are integers in the range 1 <= n, k <= 10^18.

