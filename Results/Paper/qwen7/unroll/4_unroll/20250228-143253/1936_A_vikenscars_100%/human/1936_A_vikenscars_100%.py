#!/usr/bin/python3
 
import sys
 
def ask(a, b, c, d):
	request = f"? {a} {b} {c} {d}"
	print(request, flush=True)
	return input()
	
 
def solve(n):
	max_item_idx = 0
	for i in range(1, n):
		ans = ask(max_item_idx, max_item_idx, i, i)
		if ans == "<":
			max_item_idx = i
 
	pair_idx = max_item_idx
	
	for i in range(n):
		ans1 = ask(max_item_idx, pair_idx, max_item_idx, i)
 
		if ans1 == "<":
			pair_idx = i
		elif ans1 == "=":
			ans2 = ask(pair_idx, pair_idx, i, i)
			if ans2 == ">":
				pair_idx = i
 
	print(f"! {max_item_idx} {pair_idx}")
 
t = int(input())
 
for _ in range(t):
	n = int(input())
	solve(n)