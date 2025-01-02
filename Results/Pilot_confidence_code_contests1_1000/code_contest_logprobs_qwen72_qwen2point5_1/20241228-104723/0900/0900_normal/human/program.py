for x in xrange(int(raw_input())):
    N=int(raw_input())
    print("%ld"%pow(2,bin(N).count("1")))
    