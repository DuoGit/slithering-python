import sys

cost = 117
n = 4
arr = (
    # (0, 20, 35, 42),
    # (20, 0, 34, 30),
    # (35, 34, 0, 12),
    # (42, 30, 12, 0)

    (0, 20, 35, 10),
    (20, 0, 90, 50),
    (35, 90, 0, 12),
    (10, 50, 12, 0)
)
min_cost = sys.maxsize
route = [-1 for c in range(n + 1)]
visited = [0 for v in range(n)]
result = []
skip = 0


class InitException(Exception):
    pass


def init(i: int = 0):
    if i < 0 or i >= n:
        raise InitException('Invalid start index')

    route[0] = i
    route[n] = i
    visited[i] = 1
    # route.append(start)


def update(i: int, sum: int):
    global min_cost, result

    sum += arr[i][route[0]]
    if sum < min_cost:
        min_cost = sum
        result = route.copy()


def branchbound(k: int = 1, sum: int = 0):
    global skip
    for i in range(n):
        if visited[i] == 1:
            continue

        tmp_cost = sum + arr[i][route[k - 1]]
        if tmp_cost >= min_cost:
            skip += 1
            continue

        visited[i] = 1
        pre_sum = sum
        sum = tmp_cost
        # route.append(i)
        route[k] = i

        # if len(route) == n:
        next = k + 1
        update(i, sum) if next == n else branchbound(next, sum)

        # route.pop()
        route[k] = -1
        sum = pre_sum
        visited[i] = 0


if __name__ == "__main__":
    start = 0
    init(start)

    branchbound()

    print('cost:', min_cost)
    print('skipped:', skip)
    print(result)
