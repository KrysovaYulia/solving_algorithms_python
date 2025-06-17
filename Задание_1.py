R = [(7, 1, 2), (5, 1, 3), (5, 1, 4),
     (8, 2, 4), (9, 3, 4), (5, 4, 5), (4, 4, 6), (4, 4, 7), (10, 5, 7), (8, 6, 7)]

Rs = sorted(R, key=lambda x: x[0])
U = set()
D = {}
T = []
for r in Rs:
    if r[1] not in U or r[2] not in U:
        if r[1] not in U and r[2] not in U:
            D[r[1]] = [r[1], r[2]]
            D[r[2]] = D[r[1]]
        else:
            if not D.get(r[1]):
                D[r[2]].append(r[1])
                D[r[1]] = D[r[2]]
            else:
                D[r[1]].append(r[2])
                D[r[2]] = D[r[1]]
        T.append(r)
        U.add(r[1])
        U.add(r[2])
for v in Rs:
    if v[2] not in D[v[1]]:
        T.append(v)
        gr1 = D[v[1]]
        D[v[1]] += D[v[2]]
        D[v[2]] += gr1
print(T)
print(Rs)