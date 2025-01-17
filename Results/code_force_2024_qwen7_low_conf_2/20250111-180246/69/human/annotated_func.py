#State of the program right berfore the function call: m is a positive integer representing the total number of months, x is a positive integer representing the monthly salary, and costs is a list of positive integers where costs[i] represents the cost of one unit of happiness in the i-th month.
def func_1(m, x, costs):
    costs.sort(reverse=True)
    earnings = 0
    happiness = []
    for i in range(1, m + 1):
        earnings += x
        
        while costs and costs[-1] <= earnings:
            earnings -= costs[-1]
            happiness.append(1)
            costs.pop()
        
    #State of the program after the  for loop has been executed: `m` is a positive integer, `i` is `m`, `earnings` is the initial value of `earnings` minus the sum of all elements in the final `costs` list, `happiness` is a list of length `len(happiness) + len(costs)` filled with ones, and `costs` is an empty list.
    return len(happiness)
    #`The program returns the length of the happiness list which is len(happiness) + len(costs), given that costs is an empty list, so the length is just len(happiness)`
#Overall this is what the function does:The function `func_1` accepts three parameters: `m` (the total number of months), `x` (the monthly salary), and `costs` (a list of costs associated with increasing happiness). The function first sorts the `costs` list in descending order. It then iterates through each month, accumulating earnings by adding the monthly salary. During each iteration, it checks if the highest remaining cost can be afforded with the current earnings. If so, it reduces the earnings by that cost and records a unit of happiness. This process continues until either all months have passed or no more costs can be afforded. Finally, the function returns the total number of units of happiness achieved.

