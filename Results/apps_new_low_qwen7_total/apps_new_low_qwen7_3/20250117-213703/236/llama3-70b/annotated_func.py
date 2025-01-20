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
        
    #State of the program after the loop has been executed: candies: 0, k: 3, vasya_eaten: 2n, petya_eaten: 0
#Overall this is what the function does:The function determines the smallest integer \( k \) such that if Vasya eats \( k \) candies each time and Petya eats one-tenth of the remaining candies, Vasya ends up eating at least half of the total candies \( n \). The function returns the value of \( k \) when this condition is met. If no such \( k \) is found within the given constraints (i.e., \( k \) increases indefinitely), the function will eventually break out of the loop and return the last valid \( k \) which satisfies the condition. Potential edge cases include when \( n \) is very large (up to \( 10^{18} \)), and the function may take a long time to execute.

