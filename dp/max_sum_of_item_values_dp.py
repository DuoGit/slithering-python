
item_values = []
item_weights = []
N = 0


items = []
max_value_items = []
sum_max = 0


def init(n_items: int = 1, MAX_WEIGHT: int = 1):
    N = n_items

    item_values.append(0)
    item_weights.append(0)
    for i in range(N):
        item_values.append(1)
        item_weights.append(1)

    item_values[1] = N

    # print(item_weights)
    # print(item_values)

    value_trace = [[0 for _ in range(MAX_WEIGHT + 1)] for _ in range(N + 1)]
    # print(value_trace)

    for i in range(N + 1):
        item_weight = item_weights[i]
        for j in range(MAX_WEIGHT + 1):
            skipped_item_value = 0
            selected_item_value = 0

            if i - 1 >= 0:
                skipped_item_value = value_trace[i - 1][j]
                if j - item_weight >= 0:
                    selected_item_value = item_values[i] + value_trace[i - 1][j - item_weight]

            value_trace[i][j] = max(skipped_item_value, selected_item_value)

    # print(value_trace)
    # print(value_trace[2][1])
    return value_trace


if __name__ == '__main__':
    N_items = 2
    MAX_WEIGHT = N_items - 1

    value_trace = init(N_items, MAX_WEIGHT)

    print(value_trace)

    sum_max = value_trace[N_items][MAX_WEIGHT]
    print(sum_max)

    # backtrack(MAX_WEIGHT)

    # print(max_value_items)
    # print(sum_max)
