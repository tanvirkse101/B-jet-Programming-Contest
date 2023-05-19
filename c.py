def explore(n):
    if n == 1:
        return 1
    
    return (explore(n - 1) + k - 1) % n + 1

t = int(input())

for cs in range(1, t + 1):
    n, k = map(int, input().split())
    
    print(f"Case {cs}: {explore(n)}")