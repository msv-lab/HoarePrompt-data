def solve(n):
    odd = list(range(1, n + 1, 2))    # Nieparzyste
    even = list(range(2, n + 1, 2))   # Parzyste
    p = odd + even                    # Połączenie: najpierw nieparzyste, potem parzyste
    print(*p)

# Przykład użycia
t = int(input())
while t > 0:
   n = int(input())
   solve(n)
   t -=1