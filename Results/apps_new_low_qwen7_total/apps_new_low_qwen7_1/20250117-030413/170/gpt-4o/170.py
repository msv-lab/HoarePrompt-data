n = int(input())
a = int(input())
b = int(input())
c = int(input())

if a <= b - c:
    # If plastic bottle is cheaper or same as effective cost of glass bottle
    print(n // a)
else:
    # Use as many rubles as possible to buy and return glass bottles
    k = (n - b) // (b - c) + 1  # Max number of glass bottles that can be bought and returned
    remaining_rubles = n - k * (b - c)
    
    if remaining_rubles < b:
        # If remaining rubles are less than cost of one glass bottle, buy plastic bottles
        print(k + remaining_rubles // a)
    else:
        # Otherwise, buy one more glass bottle
        print(k + 1)
