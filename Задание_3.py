x = [43, 4, 84, 70, 81, 0, 22, 94, 80, 9]

stack = [(0, len(x) - 1)]

while stack:
    low, high = stack.pop()

    if low >= high:
        continue

    mid = (low + high) // 2
    pivot = x[mid]

    left = low
    right = high

    while True:
        while x[left] < pivot:
            left += 1
        while x[right] > pivot:
            right -= 1

        if left >= right:
            break

        x[left], x[right] = x[right], x[left]
        left += 1
        right -= 1
    stack.append((right + 1, high))
    stack.append((low, right))

print(x)