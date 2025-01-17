n = int(input())
a = int(input())
b = int(input())
c = int(input())

glass = n // b
remain = n % b
kefir = glass

while remain >= c:
    new_glass = remain // c
    kefir += new_glass
    remain = new_glass + remain % c

plastic = n // a
kefir = max(kefir, plastic)

print(kefir)
