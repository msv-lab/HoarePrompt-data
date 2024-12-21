#State of the program right berfore the function call: a and b are integers such that 1 ≤ a ≤ b ≤ 10, where a represents the weight of Limak and b represents the weight of Bob.
def func():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        
        b *= 2
        
        years += 1
        
    #State of the program after the loop has been executed: 'a' is greater than 'b', `years` is the number of successful iterations, with original values ranging prior to multiplication indicating that `a` started between 1 and `b` and that `b` is less than or equal to 10.
    print(years)
#Overall this is what the function does:The function takes two integer inputs representing the weights of Limak (a) and Bob (b), where 1 ≤ a ≤ b ≤ 10. It simulates a scenario where Limak’s weight triples and Bob’s weight doubles each year until Limak’s weight surpasses Bob’s weight. The function counts the number of years it takes for Limak’s weight to become greater than Bob’s weight and returns this count as output. The final state of the function is that it prints the number of years required for Limak to outgrow Bob. Edge cases include when a and b are the same or when they are at their minimum or maximum input constraints (1, 1) and (10, 10), respectively. Additionally, the function does not handle any inputs outside the specified range, and the exact behavior is undefined in such cases.

