def min_minutes_to_equal_areas(a1, b1, a2, b2):
    from math import gcd
    
    def reduce_area(area):
        operations = 0
        while area % 2 == 0:
            area //= 2
            operations += 1
        while area % 3 == 0:
            area //= 3
            operations += 1
        return area, operations
    
    area1 = a1 * b1
    area2 = a2 * b2
    
    reduced_area1, ops1 = reduce_area(area1)
    reduced_area2, ops2 = reduce_area(area2)
    
    if reduced_area1 != reduced_area2:
        print(-1)
        return
    
    print(abs(ops1 - ops2) + min(ops1, ops2))
    print(a1, b1)
    print(a2, b2)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    a1, b1 = int(data[0]), int(data[1])
    a2, b2 = int(data[2]), int(data[3])
    min_minutes_to_equal_areas(a1, b1, a2, b2)
