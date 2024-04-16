order = {}
orders = []
n = 10
arr = [200, 10, 20, 20, 50, 50, 50, 50, 100, 100]


def cash_out(total: int, start: int = 0):
    if total <= 0:
        orders.append(order.copy())
        # print(order)
        return

    while start < n:
        if len(orders) > 0:
            return
        val = arr[start]
        if total >= val:
            order[start] = val
            cash_out(total - val, start + 1)
            order.pop(start)
        start += 1


if __name__ == "__main__":
    s = 390
    arr.sort()
    print(arr)
    cash_out(s)

    print('at most')
    for i in orders:
        print(i)

    orders.clear()
    arr.reverse()
    print(arr)
    cash_out(s)

    print('at least')
    for i in orders:
        print(i)