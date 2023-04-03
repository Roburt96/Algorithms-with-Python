def generation(index, vector):
    if index >= len(vector):
        print(*vector, sep='')
        return

    for num in range(2):
        vector[index] = num
        generation(index + 1, vector)


num = int(input())
vector = [0] * num
generation(0, vector)