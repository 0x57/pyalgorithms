def insertion_sort(numbers):
    if len(numbers) <= 0:
        return numbers
    for i in range(1, len(numbers)):
        for j in range(i, 0, -1):
            if numbers[j] < numbers[j-1]:
                numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
            else:
                break
    return numbers


if __name__ == '__main__':
    print(insertion_sort([32432,234,5,6452,53,52,1,1,2,432,21,432]))
