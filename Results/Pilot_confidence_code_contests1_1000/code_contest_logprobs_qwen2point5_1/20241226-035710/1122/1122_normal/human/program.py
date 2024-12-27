# -*- coding: utf-8 -*-
import collections

n = int(raw_input())
events = []

for i in xrange(n):
    events.append(raw_input())

counter = collections.Counter(events)
print(max(counter.values()))
