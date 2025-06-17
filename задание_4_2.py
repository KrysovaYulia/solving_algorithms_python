text = "не следует, однако, забывать"
pattern = "одна"

N = len(text)
M = len(pattern)

lps = [0] * M
j = 0
for i in range(1, M):
    while j > 0 and pattern[i] != pattern[j]:
        j = lps[j - 1]
    if pattern[i] == pattern[j]:
        j += 1
    lps[i] = j
j = 0
results = []
for c in range(N):
    while j > 0 and text[c] != pattern[j]:
        j = lps[j - 1]

    if text[c] == pattern[j]:
        j += 1

    if j == M:
        results.append(c - M + 1)
        j = lps[j - 1]

if results:
    print(f"Шаблон найден на позициях: {results}")
else:
    print("Шаблон не найден")
