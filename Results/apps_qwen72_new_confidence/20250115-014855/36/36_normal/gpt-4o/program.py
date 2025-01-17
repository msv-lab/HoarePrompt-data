def check_flag(n, m, field):
    # Check horizontal stripes
    if n % 3 == 0:
        stripe_height = n // 3
        stripe1 = field[0:stripe_height]
        stripe2 = field[stripe_height:2 * stripe_height]
        stripe3 = field[2 * stripe_height:3 * stripe_height]
        
        if (all(row == stripe1[0] for row in stripe1) and
            all(row == stripe2[0] for row in stripe2) and
            all(row == stripe3[0] for row in stripe3) and
            len(set([stripe1[0][0], stripe2[0][0], stripe3[0][0]])) == 3):
            return "YES"
    
    # Check vertical stripes
    if m % 3 == 0:
        stripe_width = m // 3
        stripe1 = [row[0:stripe_width] for row in field]
        stripe2 = [row[stripe_width:2 * stripe_width] for row in field]
        stripe3 = [row[2 * stripe_width:m] for row in field]
        
        if (all(cell == stripe1[0][0] for row in stripe1 for cell in row) and
            all(cell == stripe2[0][0] for row in stripe2 for cell in row) and
            all(cell == stripe3[0][0] for row in stripe3 for cell in row) and
            len(set([stripe1[0][0], stripe2[0][0], stripe3[0][0]])) == 3):
            return "YES"
    
    return "NO"

# Reading input
n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]

# Output the result
print(check_flag(n, m, field))
