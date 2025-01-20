#State of the program right berfore the function call: a, b, and c are non-negative integers such that 0 ≤ a, b, c ≤ 1,000,000, and x, y, and z are non-negative integers such that 0 ≤ x, y, z ≤ 1,000,000.
def func():
    a, b, c = map(int, input().split())

x, y, z = map(int, input().split())

deficit_blue = max(0, x - a)

deficit_violet = max(0, y - b)

deficit_orange = max(0, z - c)

extra_blue = max(0, a - x)

extra_violet = max(0, b - y)

extra_orange = max(0, c - z)

extra_spheres = extra_blue // 2 + extra_violet // 2 + extra_orange // 2

total_deficit = deficit_blue + deficit_violet + deficit_orange
    if (extra_spheres >= total_deficit) :
        print('Yes')
    else :
        print('No')
    #State of the program after the if-else block has been executed: *a, b, c, x, y, z, deficit_blue, deficit_violet, deficit_orange, extra_blue, extra_violet, extra_orange, extra_spheres, and total_deficit are non-negative integers. If `extra_spheres` is greater than or equal to `total_deficit`, then the function does nothing (the values remain unchanged). Otherwise, the function does nothing (the values remain unchanged as well, since there's no specific operation mentioned in the else part other than stating the condition).
#Overall this is what the function does:The function accepts no parameters and uses local variables `a`, `b`, `c`, `x`, `y`, and `z`, which are non-negative integers such that \(0 \leq a, b, c \leq 1,000,000\) and \(0 \leq x, y, z \leq 1,000,000\). It calculates the deficit and excess of each variable (`a`, `b`, `c`) compared to (`x`, `y`, `z`). Specifically, it computes the deficits where `x > a`, `y > b`, and `z > c`, and the excesses where `a > x`, `b > y`, and `c > z`. It then determines the total number of "extra" spheres available, which is half the sum of the excesses rounded down. Finally, it checks if the total number of extra spheres is sufficient to cover the total deficit. If the total number of extra spheres is enough, it prints 'Yes'; otherwise, it prints 'No'. There are no additional actions taken if the total number of extra spheres is insufficient.

