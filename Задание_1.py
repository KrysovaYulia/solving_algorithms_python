x = [43, 4, 84, 70, 81, 0, 22, 94, 80, 9]
step = len(x) // 2
while step > 0:
    for i in range(step, len(x)):
        temp = x[i]
        temp_index = i
        while temp_index >= step and x[temp_index - step] > temp:
            x[temp_index] = x[temp_index - step]
            temp_index -= step
        x[temp_index] = temp
    step //= 2

print(x)