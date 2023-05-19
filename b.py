import math

logg = [0.0] * 1000005

t = int(input())
for i in range(1, 1000001):
    logg[i] = logg[i - 1] + math.log(i)

for cas in range(1, t + 1):
    n, b = map(int, input().split())
    cnt = logg[n] / math.log(b) + 1
    print(f"Case {cas}: {int(cnt)}")