text = "не следует, однако, забывать"
pattern = "одна"

N = len(text)
M = len(pattern)

TAB = dict()
for ch in text + pattern:
    if ch not in TAB:
        TAB[ch] = M
for j in range(M - 1):
    ch = pattern[j]
    TAB[ch] = M - 1 - j

positions = [0] * N
pos_count = 0

i = M - 1
while i < N:
    k = 0

    while k < M and pattern[M - 1 - k] == text[i - k]:
        k += 1
    if k == M:
        positions[pos_count] = i - M + 1
        pos_count += 1
        i += M
    else:
        ch = text[i]
        if ch in TAB:
            shift = TAB[ch]
        else:
            shift = M
        i += shift

if pos_count == 0:
    print("Шаблон не найден")
else:
    print("Шаблон найден на позициях:", end=" ")
    print(positions[0])