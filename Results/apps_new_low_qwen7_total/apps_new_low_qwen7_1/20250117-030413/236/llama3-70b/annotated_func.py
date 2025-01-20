#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^18.
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
        
    #State of the program after the loop has been executed: `n` is 32, `k` is 5, `candies` is 0, `vasya_eaten` is 16, `petya_eaten` is 0
#Overall this is what the function does:- The function does not handle the case where \( n \) might be negative or outside the range \( 1 \leq n \leq 10^{18} \). However, given the problem constraints, it is safe to assume that valid input will always fall within this range.

