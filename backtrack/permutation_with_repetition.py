digits = (0, 1, 2)
k = 3
vector = []
permutations = []


def backtrack(i: int = 0):
    if i == k >= 0:
        permutations.append(vector.copy())
        return

    for d in digits:
        vector.append(d)
        backtrack(i+1)

        vector.pop()


if __name__ == "__main__":

    backtrack()

    print('permutation count: {}'.format(len(permutations)))
    for i in permutations:
        print(i)

