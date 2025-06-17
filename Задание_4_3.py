text = "не следует, однако, забывать"
pattern = "одна"
n = len(text)
m = len(pattern)
i = 0
found_index = -1
while i <= n - m:
    j = 0
    while j < m and not (text[i + j] < pattern[j] or pattern[j] < text[i + j]):
        j += 1
    if j == m:
        found_index = i
        break
    i += 1
if found_index + 1:
    print("Подстрока найдена на позиции", found_index)
else:
    print("Подстрока не найдена")
