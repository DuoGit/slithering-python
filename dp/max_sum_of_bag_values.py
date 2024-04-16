
bag_values = [10, 1, 1, 1, 9]
bag_weights = [1, 1, 1, 1, 1]
N = len(bag_values)

items = []
max_value_items = []
sum_max = 0


def backtrack(max_weight: int, k: int = 0, sum_values: int = 0):
    global sum_max, max_value_items

    if max_weight <= 0:
        return

    for i in range(k, N):
        next_max_weight = max_weight - bag_weights[i]

        if next_max_weight < 0:
            continue

        items.append(i)
        pre_sum_values = sum_values
        sum_values += bag_values[i]

        if sum_values > sum_max:
            sum_max = sum_values
            max_value_items = items.copy()

        backtrack(next_max_weight, i + 1, sum_values)
        sum_values = pre_sum_values
        items.pop()


if __name__ == '__main__':
    MAX_WEIGHT = 4
    backtrack(MAX_WEIGHT)

    print(max_value_items)
    print(sum_max)
