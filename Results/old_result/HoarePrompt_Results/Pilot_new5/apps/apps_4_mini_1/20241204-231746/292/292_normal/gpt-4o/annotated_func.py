#State of the program right berfore the function call: a and b are integers such that 1 ≤ a ≤ b ≤ 10, representing the weights of Limak and Bob respectively, with Limak's weight being less than or equal to Bob's weight.
def func():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        
        b *= 2
        
        years += 1
        
    #State of the program after the loop has been executed: `a` is greater than `b`, `b` is at least 80, `years` is 3.
    print(years)
#Overall this is what the function does:The function accepts two integers `a` and `b` that represent the weights of Limak and Bob, respectively. It repeatedly increases Limak's weight by multiplying it by 3 and Bob's weight by multiplying it by 2 until Limak's weight exceeds Bob's weight. It counts the number of years this process takes and prints that count. The function does not handle cases where the input values are outside the constraints (1 ≤ a ≤ b ≤ 10), nor does it validate input types.

