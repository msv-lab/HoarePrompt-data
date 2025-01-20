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
    #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are non-negative integers such that 0 ≤ `a`, `b`, `c` ≤ 1,000,000, `x`, `y`, and `z` are non-negative integers such that 0 ≤ `x`, `y`, `z` ≤ 1,000,000, `deficit_blue`, `deficit_violet`, and `deficit_orange` are non-negative integers, `extra_blue`, `extra_violet`, and `extra_orange` are non-negative integers, `extra_spheres` is a non-negative integer, `total_deficit` is a non-negative integer, and either 'Yes' is printed if `extra_spheres` is greater than or equal to `total_deficit`, or 'No' is printed if `extra_spheres` is less than `total_deficit`.
#Overall this is what the function does:The function takes six non-negative integers \(a\), \(b\), \(c\), \(x\), \(y\), and \(z\) as input and determines whether it is possible to exchange spheres between two groups such that both groups end up with the same number of blue, violet, and orange spheres. If it is possible, it prints 'Yes'; otherwise, it prints 'No'. The function does not return any value. After executing, the program state will show the values of \(a\), \(b\), \(c\), \(x\), \(y\), and \(z\) unchanged, along with the calculation of deficits and excesses in the respective colors. If the total excess spheres are enough to cover the total deficits, it prints 'Yes', otherwise 'No'.

