#!/usr/bin/env python3
import csv
import re
import operator

b = "this this this that that that that this that when when what what"
b = b.split()
print(b)
t = {}
w = {}
for i in b:
    if i[0] == "t":
    #if re.match(r't.*', i):
        t[i] = b.count(i)
    elif i[0] == "w":
        w[i] = b.count(i)
print(t)
print(w)
t = sorted(t.items(), key = operator.itemgetter(1), reverse=True)
print(t)
t.insert(0,("words", "count"))
print(t)
with open("t.csv", "w") as ta:
    writer = csv.writer(ta)
    writer.writerows(t)
