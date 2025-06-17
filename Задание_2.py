R = [(7, 1, 2), (5, 1, 3), (5, 1, 4),
     (8, 2, 4), (9, 3, 4), (5, 4, 5), (4, 4, 6), (4, 4, 7), (10, 5, 7), (8, 6, 7)]

N = 7
U = {1}
T = []
while len(U) < N:
    min_weight = 100**10
    min_edge = (-1, -1, -1)
    for edge in R:
        w, u, v = edge
        if (u in U or v in U) and not (u in U and v in U):
            if w < min_weight:
                min_weight = w
                min_edge = edge
    if min_weight == 100**10:
        break
    T.append(min_edge)
    U.add(min_edge[1])
    U.add(min_edge[2])
print(T)
