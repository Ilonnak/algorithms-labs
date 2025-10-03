comparisons = 0
assignments = 0
recursive_calls = 0

def partition(arr, l, r):
    global comparisons, assignments
    pivot = arr[l]
    assignments += 1
    i = l - 1
    j = r + 1
    while True:
        while True:
            i += 1
            comparisons += 1
            if arr[i] >= pivot:
                break
        while True:
            j -= 1
            comparisons += 1
            if arr[j] <= pivot:
                break
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]
        assignments += 2

def quicksort(arr, l, r):
    global recursive_calls
    if l < r:
        recursive_calls += 1
        q = partition(arr, l, r)
        quicksort(arr, l, q)
        quicksort(arr, q + 1, r)

arr = [47, 50, 61, 41, 53, 12, 68, 63, 3]
print("Початковий масив:", arr)

quicksort(arr, 0, len(arr) - 1)

print("Відсортований масив:", arr)
print("Загальна кількість порівнянь:", comparisons)
print("Загальна кількість присвоєнь:", assignments)
print("Загальна кількість рекурсивних викликів:", recursive_calls)
