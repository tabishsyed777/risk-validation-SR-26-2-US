import math
from collections import Counter, defaultdict
def accuracy(rows): return sum(r["expected"] == r["predicted"] for r in rows) / len(rows) if rows else 0.0
def psi(reference, current):
    labels=set(reference)|set(current); r,c=Counter(reference),Counter(current); tr,tc=max(sum(r.values()),1),max(sum(c.values()),1)
    return sum(((c[x]/tc)-(r[x]/tr))*math.log(max(c[x]/tc,1e-6)/max(r[x]/tr,1e-6)) for x in labels)
def segment_accuracy(rows):
    groups=defaultdict(list)
    for row in rows: groups[row["segment"]].append(row)
    return {key:accuracy(value) for key,value in groups.items()}
