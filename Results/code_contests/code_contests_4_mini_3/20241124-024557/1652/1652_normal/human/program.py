import sys

nb_test = 0

idx = 0
for line in sys.stdin:
    if idx != 0:
        list_divisors = map(int, line.strip().split(" "))
        a, b = list_divisors[0], list_divisors[1]
        a, b = (b, a) if a > b else (a, b)

        for d in list_divisors[2:]:
            if d >= b:
                if d % b == 0:
                    b = d
                elif d % a == 0:
                    a = d

                a, b = (b, a) if a > b  else (a, b)
            else:
                if d >= a:
                    if d % a == 0:
                        a = d

        sys.stdout.write("%d %d\n" % (a, b))
    idx += 1
