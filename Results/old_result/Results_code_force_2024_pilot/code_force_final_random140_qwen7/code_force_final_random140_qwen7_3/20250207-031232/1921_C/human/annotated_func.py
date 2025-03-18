#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, f, a, and b are integers such that 1 ≤ n ≤ 2 ⋅ 10^5, 1 ≤ f, a, b ≤ 10^9. The list m contains n integers such that 1 ≤ m_i ≤ 10^9 and m_i < m_{i+1}.
def func():
    t = int(input())
    for _ in range(t):
        n, f, a, b = map(int, input().split())
        
        arr = [0] + list(map(int, input().split()))
        
        possible = True
        
        for i in range(1, n + 1):
            time_diff = arr[i] - arr[i - 1]
            energy_keep_on = a * time_diff
            energy_turn_off_on = b
            energy_cost = min(energy_keep_on, energy_turn_off_on)
            if f <= energy_cost:
                possible = False
                break
            f -= energy_cost
        
        print('YES' if possible else 'NO')
        
    #State: Output State: `f` is `f - total_energy_cost`, `i` is `n + 1`, `possible` is `False`.
    #
    #After the loop executes all its iterations, the variable `f` will have been reduced by the total energy cost (`total_energy_cost`) calculated over all iterations. The value of `i` will be `n + 1`, indicating that the loop has completed all its iterations. The variable `possible` will be set to `False` because the loop eventually sets it to `False` when `f` becomes insufficient to cover the `energy_cost` for any iteration.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads integers `n`, `f`, `a`, and `b` along with a list `m` of `n` integers. It then calculates the energy cost to keep a device on or turn it off at each step and checks if the available energy `f` is sufficient to cover these costs without depleting below zero. If `f` ever falls below the required energy cost, it sets `possible` to `False`. After processing all test cases, it prints 'YES' if `possible` remains `True` for all cases, otherwise it prints 'NO'. The function modifies the input variable `f` by subtracting the total energy cost across all iterations.

