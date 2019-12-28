def cocktail_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    i, j = 0, len(numbers)-1
    while i < j:
        for k in range(i, j):
            if numbers[k] > numbers[k+1]:
                numbers[k], numbers[k+1] = numbers[k+1], numbers[k]
        j -= 1
        for k in range(j, i, -1):
            if numbers[k] < numbers[k-1]:
                numbers[k], numbers[k-1] = numbers[k-1], numbers[k]
        i += 1
    return numbers


if __name__ == '__main__':
    print(cocktail_sort([2,343,23,63,45,4352,43,4326,2542,23]))
