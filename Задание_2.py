x = [43, 4, 84, 70, 81, 0, 22, 94, 80, 9]
width = 1
n = len(x)
while width < n:
    left = 0
    while left + width < n:
        right = min(left + 2 * width - 1, n - 1)
        mid = left + width - 1
        left_part = x[left:mid + 1]
        right_part = x[mid + 1:right + 1]
        i = 0
        j = 0
        k = left
        while i < len(left_part) and j < len(right_part):
            if left_part[i] <= right_part[j]:
                x[k] = left_part[i]
                i += 1
            else:
                x[k] = right_part[j]
                j += 1
            k += 1
        while i < len(left_part):
            x[k] = left_part[i]
            i += 1
            k += 1
        while j < len(right_part):
            x[k] = right_part[j]
            j += 1
            k += 1
        left += 2 * width
    width *= 2
print("Отсортированный массив:", x)