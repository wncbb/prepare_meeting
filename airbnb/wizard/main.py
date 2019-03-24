def min_distance(wizards, start=0, end=9):
     # info = collections.defaultdict(set)
    # for idx, wizard in enumerate(wizards):
    #     info[idx] = set(wizard)
    cur_level = {start: 0}
    ans = 0x7FFFFFFF
    for _ in xrange(10):
        next_level = {}
        for idx, cur_cost in cur_level.iteritems():
            if idx >= len(wizards):
                continue
            for nx in wizards[idx]:
                cost = cur_cost + (nx - idx) ** 2
                if nx == end:
                    ans = min(ans, cost)
                else:
                    if nx not in next_level:
                        next_level[nx] = cost
                    else:
                        next_level[nx] = min(next_level[nx], cost)
        cur_level = next_level
    return ans
