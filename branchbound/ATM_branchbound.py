import math

order = {}
orders = []
n = 10
arr = (200, 10, 20, 20, 50, 50, 50, 50, 100, 100)
arr_max = [e for e in arr]
filterCount = 0


def form_max_arr():
    maxVal = 0
    for i in range(n - 1, 0, -1):
        if maxVal < arr[i]:
            maxVal = arr[i]
        arr_max[i] = maxVal

    print(arr_max)


def cash_out(total: int, start: int = 0):
    global filterCount

    if total <= 0:
        orders.append(order.copy())
        # print(order)
        return

    while start < n:
        if (math.ceil(total / arr_max[start])) > (n - start + 1):
            filterCount += 1
            return

        val = arr[start]
        if total >= val:
            order[start] = val
            cash_out(total - val, start + 1)
            order.pop(start)
        start += 1


if __name__ == "__main__":
    form_max_arr()

    s = 390
    cash_out(s)

    print('count: {:d}'.format(len(orders)))
    print('excluded: {}'.format(filterCount))
    for i in orders:
        print(i)
