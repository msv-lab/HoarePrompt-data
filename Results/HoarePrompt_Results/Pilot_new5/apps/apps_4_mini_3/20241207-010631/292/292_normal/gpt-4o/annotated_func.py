#State of the program right berfore the function call: a and b are integers such that 1 ≤ a ≤ b ≤ 10, representing the weights of Limak and Bob respectively, where Limak's weight is less than or equal to Bob's weight.
def func():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        
        b *= 2
        
        years += 1
        
    #State of the program after the loop has been executed: `a` is greater than `b`, `years` is at least 3, the final value of `a` is greater than 120, and the final value of `b` is less than 80.
    print(years)
#Overall this is what the function does:The function accepts two integers `a` and `b` representing the weights of Limak and Bob, respectively. It calculates how many years it will take for Limak's weight to exceed Bob's, given that Limak's weight triples and Bob's weight doubles each year. The function then prints the total number of years required for Limak's weight to surpass Bob's weight.

