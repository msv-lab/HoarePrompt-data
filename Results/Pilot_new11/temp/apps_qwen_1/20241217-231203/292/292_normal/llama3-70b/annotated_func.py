#State of the program right berfore the function call: a and b are positive integers such that 1 <= a <= b <= 10.
def func():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        
        b *= 2
        
        years += 1
        
    #State of the program after the loop has been executed: `a` is between 3<sup>years</sup> and 30<sup>years</sup>, `b` is between 2<sup>years</sup> and 20<sup>years</sup>, `years` is the number of times the loop executed.
    print(years)
#Overall this is what the function does:The function reads two positive integers \(a\) and \(b\) (where \(1 \leq a \leq b \leq 10\)) from the user, then enters a loop where \(a\) is tripled and \(b\) is doubled in each iteration. The loop continues until \(a\) exceeds \(b\). After the loop ends, the function prints the number of iterations performed. The final state of the program is that the output is the number of iterations, and \(a\) and \(b\) are no longer within the initial constraints \(1 \leq a \leq b \leq 10\).

