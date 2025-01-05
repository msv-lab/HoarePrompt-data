
T=int(input())
for x in range(T):
    N=int(input())
    liczba=int(input())
    wynik=liczba
    akt=10
    while akt<liczba:
        wynik+=liczba//akt
        akt*=10
    print(wynik)