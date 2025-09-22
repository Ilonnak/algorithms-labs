def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    for i in range(n - 1):
        min_index = i
        assignments += 1
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
                assignments += 1
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            assignments += 3

    return arr, comparisons, assignments


def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    for i in range(1, n):
        key = arr[i]
        assignments += 1
        j = i - 1
        assignments += 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            assignments += 1
            j -= 1
            assignments += 1
        if j >= 0:
            comparisons += 1
        arr[j + 1] = key
        assignments += 1

    return arr, comparisons, assignments


data = [53, 100, 44, 74, 53, 38, 82, 65, 28]

print("Оригінальний масив:", data)

sorted_selection, comps_sel, assigns_sel = selection_sort(data.copy())
print("\nSelection Sort:")
print("Відсортований масив:", sorted_selection)
print("Кількість порівнянь:", comps_sel)
print("Кількість присвоєнь:", assigns_sel)

sorted_insertion, comps_ins, assigns_ins = insertion_sort(data.copy())
print("\nInsertion Sort:")
print("Відсортований масив:", sorted_insertion)
print("Кількість порівнянь:", comps_ins)
print("Кількість присвоєнь:", assigns_ins)
