# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 06:49:50 2022

@author: svale

Programming Praxis
Penniless Pilgrim
August 10, 2018

Borrowed from Daniel's Python solution - especially elegant!

q - queue, list of tuples consisting of the following
    c - cost
    x - horizontal position on grid, [0, 4] valid
    y - vertical position on grid, [0, 4] valid
    p - path string sequence, 'news' = north east west south
    e - numeric identification of single path edge

"""

from fractions import Fraction

q = [(Fraction(4), 2, 0, 'ee', set([(1,0),(3,0)]))]
#q = [(Fraction(2), 1, 0, 'e', set([(1,0)]))]

count = 0
while q:
    c,x,y,p,e = q.pop()
    if (len(p) != len(e) or not (x in range(0,5) and y in range(0,5))):
        continue
    if (x == 4 and y == 4 and c == 0):
        print(p)
        count = count + 1
    q.append((c+2.0, x+1, y, p+'e', e|set([(2*x+1,2*y)])))
    q.append((c-2.0, x-1, y, p+'w', e|set([(2*x-1,2*y)])))
    q.append((c*2.0, x, y+1, p+'s', e|set([(2*x,2*y+1)])))
    q.append((c/2.0, x, y-1, p+'n', e|set([(2*x,2*y-1)])))
