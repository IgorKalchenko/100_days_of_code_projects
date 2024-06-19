N, M = input().split()
N = int(N)
M = int(M)
c = [int(input()) for _ in range(N)]
min_value = 0
max_value = int(1e8)
while max_value -min_value > 1:
    mid_value = (min_value + max_value) // 2
    if sum([c[i] // mid_value for i in range(N)]) < M:
        max_value = mid_value
    else:
        min_value = mid_value
print(min_value)