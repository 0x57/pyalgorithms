def bubble_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    for i in range(len(numbers) - 1, 0, -1):
        for j in range(i):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


if __name__ == '__main__':
    print(bubble_sort([2,4,6,1,2,3,6,2,1,45,76,3,23,5,34,2,5]))
