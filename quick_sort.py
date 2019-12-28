def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    mid = numbers[0]
    left = []
    right = []
    for i in numbers[1:]:
        if i <= mid:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left) + [mid] + quick_sort(right)


if __name__ == '__main__':
    print(quick_sort([2,3432.34,5.1,2,65,3.23,.5432]))
