#State of the program right berfore the function call: a, b, c, x, y, z are non-negative integers such that 0 ≤ a, b, c, x, y, z ≤ 1,000,000.
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
    #State of the program after the if-else block has been executed: *a, b, c, x, y, z, deficit_blue, deficit_violet, deficit_orange, extra_blue, extra_violet, extra_orange, extra_spheres, and total_deficit retain their original values. If extra_spheres is greater than or equal to total_deficit, 'Yes' is printed. Otherwise, no output is produced.
#Overall this is what the function does:This function reads two sets of three non-negative integers each (a, b, c and x, y, z) from user input, where each integer is within the range 0 ≤ n ≤ 1,000,000. It calculates the deficits (if x > a, y > b, or z > c) and the surplus (if a > x, b > y, or c > z) of each pair. The surplus values are halved and summed up to determine if the total surplus can cover the total deficit. If the total surplus is greater than or equal to the total deficit, the function prints 'Yes'; otherwise, it prints 'No'. After execution, the variables a, b, c, x, y, z, deficit_blue, deficit_violet, deficit_orange, extra_blue, extra_violet, extra_orange, extra_spheres, and total_deficit retain their values.

