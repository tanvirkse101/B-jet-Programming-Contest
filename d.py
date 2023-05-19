def explore(n):
    if n == 1:
        return 1
    
    return (explore(n - 1) + k - 1) % n + 1

t = int(input())

for cs in range(1, t + 1):
    n = int(input())
    k = int(input())
    
    print("Case {}: {}".format(cs, explore(n)))