#State of the program right berfore the function call: a, b, c, x, y, z are non-negative integers such that 0 <= a, b, c, x, y, z <= 1,000,000.
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
    #State of the program after the if-else block has been executed: *`a` is A, `b` is B, `c` is C, `x` is X, `y` is Y, `z` is Z, `deficit_blue` is max(0, X - A), `deficit_violet` is max(0, Y - B), `deficit_orange` is max(0, Z - C), `extra_blue` is max(0, A - X), `extra_violet` is max(0, B - Y), `extra_orange` is max(0, C - Z), `extra_spheres` is extra_blue // 2 + extra_violet // 2 + extra_orange // 2, `total_deficit` is deficit_blue + deficit_violet + deficit_orange, if `extra_spheres` is greater than or equal to `total_deficit`, the print statement outputs 'Yes'. Otherwise, the print statement indicates that `extra_spheres` is less than `total_deficit`.
#Overall this is what the function does:The function reads six non-negative integers \(a\), \(b\), \(c\), \(x\), \(y\), and \(z\) from the standard input, where each integer is within the range \([0, 1,000,000]\). It then calculates the deficit of blue, violet, and orange spheres as \(x - a\), \(y - b\), and \(z - c\), respectively, ensuring the deficits are non-negative. Similarly, it calculates the excess of blue, violet, and orange spheres as \(a - x\), \(b - y\), and \(c - z\), again ensuring the excesses are non-negative. The function then computes the total number of extra spheres available, which is the sum of half the excess blue, violet, and orange spheres. Finally, it checks if the total number of extra spheres is sufficient to cover the total deficit. If the extra spheres are enough to cover the deficit, it prints 'Yes'; otherwise, it prints 'No'.

