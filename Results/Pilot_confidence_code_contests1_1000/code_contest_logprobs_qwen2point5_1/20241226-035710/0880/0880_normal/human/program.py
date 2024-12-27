#!/usr/bin/env python
# coding: utf-8

if __name__ == '__main__':
    import sys
    f = sys.stdin
    #f = open('/home/ilya/opt/programming/tasks/724D.txt')
    
    if False:
        import StringIO
        f = StringIO.StringIO("""3
bcabcbaccba""")
        
    if False:
        import StringIO
        f = StringIO.StringIO("""2
abcab""")
        

    def read_int_line():
        return map(int, next(f).split())

    m = read_int_line()[0]
    line =  next(f)
    
    import bisect
    def upper_bound(indexes, idx, lo):
        return bisect.bisect_right(indexes, idx, lo)

    def find_seq(line): 
        ln = len(line)
        
        min_c = None
        indexes = []
        min_ok = True
        for i, c in enumerate(line):
            if min_c is None:
                min_c = c
                indexes = [i]
            else:
                diff = ord(c) - ord(min_c)
                if diff < 0:
                    min_c = c
                    indexes = [i]
                    min_ok = min_ok and i < m
                elif diff == 0:
                    if min_ok:
                        if indexes:
                            last = indexes[-1]
                            min_ok = (i - last) <= m
                    indexes.append(i)
                
            
        assert indexes
        min_ok = min_ok and (i - indexes[-1]) < m
        
        idx_ln = len(indexes)
        if min_ok:
            cnt = 0
            
            lo = 0
            value = m - 1
            while lo < idx_ln:
                idx = upper_bound(indexes, value, lo)
                cnt += 1
                
                if idx < idx_ln:
                    value = indexes[idx] + m
                    lo += 1
                else:
                    break

            lst = [(min_c, cnt)]
        else:
            # остальные
            lst = [(min_c, idx_ln)]
            
            def append_range(previous, idx):
                # :TODO: memoryview
                subline = line[previous+1:idx]
                lst.extend(find_seq(subline))
            
            previous = 0
            for idx in indexes:
                if idx - previous > m:
                    append_range(previous, idx)
                    
                previous = idx
                
            if ln - previous > m:
                append_range(idx, ln)
                
        return lst

    def print_subrange(c, cnt):
        pass #sys.stdout.write("".join(c for i in xrange(cnt)))

    lst = find_seq(line)
    
    # вывод
    lst.sort()
    
    prev_c, prev_cnt = None, 0
    for c, cnt in lst:
        if not prev_cnt:
            prev_c, prev_cnt = c, cnt
        else:
            if c != prev_c:
                print_subrange(prev_c, prev_cnt)
                prev_c, prev_cnt = c, cnt
            else:
                prev_cnt += cnt

    assert prev_cnt
    print_subrange(prev_c, prev_cnt)
    