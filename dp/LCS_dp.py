def indices_to_index(trace, row_length: int):
    return trace[0] * row_length + trace[1]


def index_to_indices(index: int, row_length: int):
    return index // row_length, index % row_length


def find_lcs(s_row: str, s_col: str):
    rows = len(s_col)
    row_length = len(s_row)

    # test = [[{"i": 0}] * m_cols] * n_rows
    # trace = [[{0: -1, 1: -1}] * (m_cols+1)] * (n_rows+1)
    # max_str_len_at = [[0] * (m_cols+1)] * (n_rows+1)

    # trace = [[{0: i, 1: j} for j in range(row_length + 1)] for i in range(rows + 1)]
    trace = [[{0: -1, 1: -1} for _ in range(row_length + 1)] for _ in range(rows + 1)]

    max_str_len_at = [[0 for _ in range(row_length + 1)] for _ in range(rows + 1)]

    # trail = [[{0: i, 1: j} for j in range(row_length + 1)] for i in range(rows + 1)]
    trail = [[{0: -1, 1: -1} for _ in range(row_length + 1)] for _ in range(rows + 1)]

    linked_map = {}
    # trace = []
    # max_str_len_at = []
    # for i in range(rows+1):
    #     sub_trace = []
    #     sub_max = []
    #     for j in range(row_length+1):
    #         sub_trace.append({0: i, 1: j})
    #         sub_max.append(0)
    #     trace.append(sub_trace)
    #     max_str_len_at.append(sub_max)

    # print(test)
    # print(trace)
    # print(max_str_len_at)

    start = {0: -1, 1: -1}
    for i in range(rows - 1, -1, -1):
        for j in range(row_length - 1, -1, -1):

            x = 1 if s_row[j] == s_col[i] else 0

            if x < max_str_len_at[i][j + 1]:
                row_max = trace[i][j + 1][0]
                if row_max == i:
                    max_str_len_at[i][j] = max_str_len_at[i][j + 1]
                elif row_max > i:
                    max_str_len_at[i][j] = max_str_len_at[i][j + 1] + x

                if x == 0:
                    trace[i][j] = trace[i][j + 1]
                elif x == 1:
                    trace[i][j][0] = i
                    trace[i][j][1] = j
                    trail[i][j] = trace[i][j + 1]
                    linked_map[i * row_length + j] = indices_to_index(trace[i][j + 1], row_length)
                    if row_max > i:
                        start[0] = i
                        start[1] = j
            else:
                max_str_len_at[i][j] = x
                trace[i][j][0] = i
                trace[i][j][1] = j
                start[0] = i
                start[1] = j

            if max_str_len_at[i][j] < max_str_len_at[i + 1][j + 1] + x:
                max_str_len_at[i][j] = max_str_len_at[i + 1][j + 1] + x
                trace[i][j][0] = i
                trace[i][j][1] = j
                linked_map[i * row_length + j] = indices_to_index(trace[i + 1][j + 1], row_length)
                trail[i][j] = trace[i + 1][j + 1]

                start[0] = i
                start[1] = j

            if max_str_len_at[i][j] < max_str_len_at[i + 1][j]:
                col_max = trace[i + 1][j][1]
                if col_max == j:
                    max_str_len_at[i][j] = max_str_len_at[i + 1][j]
                elif col_max > j:
                    max_str_len_at[i][j] = max_str_len_at[i + 1][j] + x

                if x == 0:
                    trace[i][j] = trace[i + 1][j]
                elif x == 1:
                    trace[i][j][0] = i
                    trace[i][j][1] = j
                    linked_map[i * row_length + j] = indices_to_index(trace[i + 1][j], row_length)
                    trail[i][j] = trace[i + 1][j]
                    if col_max > j:
                        start[0] = i
                        start[1] = j

    i, j = start[0], start[1]
    # while trail[i][j][0] != i and trail[i][j][1] != j:
    #     print("{}({}, {})".format(s_row[j], i, j))
    #     i, j = trail[i][j][0], trail[i][j][1]
    # else:
    #     print("{}({}, {})".format(s_row[j], i, j))

    if i != -1 and j != -1:
        # while trail[i][j][0] != -1 and trail[i][j][1] != -1:
        #     print("{}({}, {})".format(s_row[j], i, j))
        #     i, j = trail[i][j][0], trail[i][j][1]
        # else:
        #     print("{}({}, {})".format(s_row[j], i, j))

        k = -1
        v = indices_to_index(start, row_length)
        linked_map[k] = v
        print(linked_map)

        while linked_map.get(k) is not None:
            v = linked_map[k]
            i, j = index_to_indices(v, row_length)
            print("{}({}, {})".format(s_row[j], i, j))
            k = v


if __name__ == "__main__":
    # s_row = "aabb"
    # s_col = "aab"

    s_row = "ba"
    s_col = "bbba"
    find_lcs(s_row, s_col)

    end = {0: -1, 1: -1}
    start = end.copy()

    start[0] = 0

    print(end)
