#State of the program right berfore the function call: a and b are integers such that 2 ≤ a, b ≤ 20 and gcd(a, b) is the greatest common divisor of a and b.
def func_1(a, b):
    return a * b // gcd(a, b)
    #The program returns the product of a and b divided by their greatest common divisor (gcd)
#Overall this is what the function does:The function accepts two integer parameters `a` and `b`, both within the range of 2 to 20 inclusive, and returns their least common multiple (LCM). This is calculated by dividing the product of `a` and `b` by their greatest common divisor (gcd).

#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 50, and vals is a list of N integers where each integer k_i satisfies 2 ≤ k_i ≤ 20.
def func_2():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    den = vals[0]
    for x in vals:
        den = func_1(den, x)
        
    #State: Output State: `vals` is an empty list or has no elements left to iterate over; `den` is the final result obtained by successively applying the `func_1(den, x)` function to each element `x` in the original list `vals`.
    #
    #In natural language, after the loop has executed all its iterations, the list `vals` will be exhausted (i.e., it will be empty), and the variable `den` will hold the cumulative result of applying the `func_1` function to each element of the original list `vals`, starting with the initial value of `den`.
    vprod = [(den // r) for r in vals]
    den = den - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns None
    #State: `vals` is an empty list; `den` is `den - sum(vprod)`. `den` is greater than 0
    print(' '.join([str(x) for x in vprod]))
    #This is printed: ' '.join([str(x) for x in vprod]) (where vprod is a list of numbers whose sum is subtracted from den)
#Overall this is what the function does:The function reads two lines of input: the first line contains an integer \(N\) representing the size of the list, and the second line contains \(N\) space-separated integers. It then calculates a cumulative result using the `func_1` function on these integers, storing the result in `den`. After processing, it computes a new list `vprod` based on `den` and the original list `vals`. If `den` becomes less than or equal to zero after adjusting it with `vprod`, it prints `-1` and returns. Otherwise, it prints the elements of `vprod` as a space-separated string and returns `None`.

