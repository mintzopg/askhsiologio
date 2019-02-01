import itertools as it

# Enter your code here. Read input from STDIN. Print output to STDOUT
k, m = map(int, input().split())
n = [list(map(int, input().split())).pop(0) for _ in range(k)]
print(max(
    map(lambda K_i: sum(n_i**2 for n_i in K_i) % m, it.product(*n)))
)
