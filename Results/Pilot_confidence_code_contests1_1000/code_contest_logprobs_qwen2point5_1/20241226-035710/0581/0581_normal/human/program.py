#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout

class TeamResult:
    
    def __init__(self):
        self.points = 0
        self.goals_scored = 0
        self.goals_missed = 0
        
    def update(self,scored,missed):
        if scored > missed:
            self.points += 3
        elif scored == missed:
            self.points += 1
        self.goals_scored += scored
        self.goals_missed += missed
    
    def to_tuple(self):
        return (self.points,self.goals_missed,self.goals_missed)
    

def solve(teams,matches):
    
    for m in matches:
        tr1,tr2 = m
        name1,goals1 = tr1
        name2,goals2 = tr2
        teams[name1].update(goals1,goals2)
        teams[name2].update(goals2,goals1)
    
    T = [(name,tr.to_tuple()) for name,tr in teams.iteritems()]
    
    T.sort(key=lambda t: t[1], reverse=True)
    #print T

    n = len(T)
    T_names = [t[0] for t in T[:(n/2)] ]
    return sorted(T_names)


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d) if len(s.strip())>0]


n = int(ifs.readline())

teams = {}
for _ in range(n):
    name = ifs.readline().strip()
    teams[name] = TeamResult()

matches = []
for _ in range(n*(n-1)/2):
    marks,goals = ifs.readline().strip().split(' ')
    t1,t2 = marks.split('-')
    g1,g2 = goals.split(':')
    matches.append( ((t1,int(g1)), (t2,int(g2))) )

winners = solve(teams,matches)

for name in winners:
    ofs.write('%s\n' % name)
