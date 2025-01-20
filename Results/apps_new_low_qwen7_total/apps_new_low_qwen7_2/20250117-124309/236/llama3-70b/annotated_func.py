#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^18.
def func():
    n = int(input())

k = 1
    while True:
        candies = n
        
        vasya_eaten = 0
        
        while candies > 0:
            vasya_eaten += min(k, candies)
            candies -= min(k, candies)
            petya_eaten = candies // 10
            candies -= petya_eaten
        
        if vasya_eaten * 2 >= n:
            print(k)
            break
        
        k += 1
        
    #State of the program after the loop has been executed: `vasya_eaten` is the total amount of candies eaten by Vasya, `petya_eaten` is the total amount of candies eaten by Petya, `candies` is 0, `k` is the last value of `k` for which the condition `vasya_eaten * 2 < n` holds, and `n` is a non-negative integer.
#Overall this is what the function does:The function determines the minimum integer value of `k` such that if Vasya eats candies according to the rule (taking up to `k` candies each turn) and Petya eats one-tenth of the remaining candies each turn, Vasya ends up eating at least twice as many candies as the total number of candies initially divided among them. The function returns this integer value `k`. If no such `k` is found within a reasonable range (up to \(10^{18}\)), the function will still terminate and return the last valid `k` value where Vasya’s total candies are less than double the initial number of candies.

