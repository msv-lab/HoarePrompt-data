#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each set of input data, n and k are integers such that 1 ≤ k < n ≤ 10^5, and for each edge described by v and u, 1 ≤ v, u ≤ n. The sum of the values of n for all sets of input data does not exceed 10^5.
def func_1():
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4. After executing the loop, t remains unchanged, and no new variables or states are introduced within the loop. Each iteration of the loop calls the `solve()` function with input data, but the loop itself does not modify any external state variables. Therefore, the only variable that retains its initial state is t.
#Overall this is what the function does:The function processes multiple sets of input data where each set contains integers \( t \), \( n \), \( k \), and edges defined by pairs \( (v, u) \). It calls the `solve()` function for each set of input data without modifying any external state variables. The function does not return any value; instead, it outputs results based on the processing of the input data. The only variable that retains its initial state is \( t \), which is an integer such that \( 1 \leq t \leq 10^4 \).

