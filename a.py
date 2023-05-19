import math
import sys

t = int(sys.stdin.readline())
k = 0

for _ in range(t):
    n = int(sys.stdin.readline())
    sq = math.ceil(math.sqrt(n))
    r = sq*sq - n
    if r < sq:
        b = r + 1
        a = sq
    else:
        a = 2*sq - r - 1
        b = sq
    if sq % 2 == 1:
        a, b = b, a
    print("Case {}: {} {}".format(k+1, a, b))
    k += 1