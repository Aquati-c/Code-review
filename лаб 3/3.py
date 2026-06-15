from collections import deque

def solve(file_name, K, L):
    with open(file_name, "r") as f:
        n = int(f.readline())
        g = [list(map(int, f.readline().split())) for _ in range(n)]

    K -= 1  # перевод в 0-индексацию

    dist = [-1] * n
    q = deque()

    q.append(K)
    dist[K] = 0

    while q:
        v = q.popleft()

        if dist[v] == L:
            continue  # дальше идти нельзя

        for to in range(n):
            if g[v][to] == 1 and dist[to] == -1:
                dist[to] = dist[v] + 1
                q.append(to)

    result = [i + 1 for i in range(n) if 0 < dist[i] <= L]

    if not result:
        print(-1)
    else:
        print(*sorted(result))
"""
ChatGPT
"""