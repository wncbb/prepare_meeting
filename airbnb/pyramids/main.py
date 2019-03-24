import collections

def generate_status(all_status, matrix):
    if len(all_status) == 1:
        return all_status[0]

    next_all_status = []
    for i in xrange(len(all_status) - 1):
        cur_status = set()
        for first in all_status[i]:
            for second in all_status[i + 1]:
                cur_status |= set(list(matrix[first][second]))
        next_all_status.append(cur_status)

    return generate_status(next_all_status, matrix)


def is_legal_status(nodes, status, matrix):
    all_status = [set(node) for node in nodes]
    print all_status
    return status in generate_status(all_status, matrix)

nodes = "ABCD"
matrix = collections.defaultdict(lambda: collections.defaultdict(list))
matrix['A']['A'] = ['B']
matrix['A']['B'] = ['A', 'C']
matrix['A']['C'] = ['D']
matrix['A']['D'] = ['A']
matrix['B']['A'] = ['D']
matrix['B']['B'] = ['B', 'C']
matrix['B']['C'] = ['A']
matrix['C']['D'] = ['B']
print is_legal_status(nodes, 'D', matrix)
