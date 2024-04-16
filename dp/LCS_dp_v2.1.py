def index_from_indices(trace, row_length: int):
    return trace[0] * row_length + trace[1]


def indices_from_index(index: int, row_length: int):
    return index // row_length, index % row_length


def find_lcs(s_row: str, s_col: str):
    rows = len(s_col)
    cols = len(s_row)

    # test = [[{"i": 0}] * m_cols] * n_rows
    # trace = [[{0: -1, 1: -1}] * (m_cols+1)] * (n_rows+1)
    # max = [[0] * (m_cols+1)] * (n_rows+1)

    trace = [[{0: i, 1: j} for j in range(cols + 1)] for i in range(rows + 1)]
    max = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
    track = []

    trail = [[{0: i, 1: j} for j in range(cols + 1)] for i in range(rows + 1)]
    link = {}
    # trace = []
    # max = []
    # for i in range(rows+1):
    #     sub_trace = []
    #     sub_max = []
    #     for j in range(cols+1):
    #         sub_trace.append({0: i, 1: j})
    #         sub_max.append(0)
    #     trace.append(sub_trace)
    #     max.append(sub_max)

    # print(test)
    # print(trace)
    # print(max)

    start = {0: -1, 1: -1}
    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):

            x = 1 if s_row[j] == s_col[i] else 0

            if x < max[i][j + 1]:
                row_max = trace[i][j + 1][0]
                if row_max == i:
                    max[i][j] = max[i][j + 1]
                elif row_max > i:
                    max[i][j] = max[i][j + 1] + x

                # trace[i][j] = trace[i][j+1]

                # max[i][j] = max[i][j + 1] + x
                if x == 0:
                    trace[i][j] = trace[i][j + 1]
                elif x == 1:
                    trace[i][j][0] = i
                    trace[i][j][1] = j
                    trail[i][j] = trace[i][j + 1]
                    link[i * cols + j] = index_from_indices(trace[i][j + 1], cols)
                    if row_max > i:
                        track.append(trace[i][j + 1])
                        # track.append(trace[i][j])
                        start[0] = i
                        start[1] = j
            else:
                max[i][j] = x
                # trace[i][j][0] = i
                # trace[i][j][1] = j

            if max[i][j] < max[i + 1][j + 1] + x:
                max[i][j] = max[i + 1][j + 1] + x
                # trace[i][j] = trace[i+1][j+1]
                trace[i][j][0] = i
                trace[i][j][1] = j
                link[i * cols + j] = index_from_indices(trace[i + 1][j + 1], cols)
                trail[i][j] = trace[i + 1][j + 1]

                track.append(trace[i + 1][j + 1])
                # track.append(trace[i][j])
                start[0] = i
                start[1] = j

            if max[i][j] < max[i + 1][j]:
                col_max = trace[i + 1][j][1]
                if col_max == j:
                    max[i][j] = max[i + 1][j]
                elif col_max > j:
                    max[i][j] = max[i + 1][j] + x

                if x == 0:
                    trace[i][j] = trace[i + 1][j]
                elif x == 1:
                    trace[i][j][0] = i
                    trace[i][j][1] = j
                    link[i * cols + j] = index_from_indices(trace[i + 1][j], cols)
                    trail[i][j] = trace[i + 1][j]
                    if col_max > j:
                        track.append(trace[i + 1][j])
                        # track.append(trace[i][j])
                        start[0] = i
                        start[1] = j

    # print(max)

    i, j = start[0], start[1]
    while trail[i][j][0] != i and trail[i][j][1] != j:
        print("{}({}, {})".format(s_row[j], i, j))
        i, j = trail[i][j][0], trail[i][j][1]
    else:
        print("{}({}, {})".format(s_row[j], i, j))

    k = -1
    v = index_from_indices(start, cols)
    link[k] = v
    print(link)

    while link.get(k) is not None:
        v = link[k]
        i, j = indices_from_index(v, cols)
        print("{}({}, {})".format(s_row[j], i, j))
        k = v


if __name__ == "__main__":
    # s_row = "aabb"
    # s_col = "aab"

    s_row = "aabb"
    s_col = "abb"
    find_lcs(s_row, s_col)
