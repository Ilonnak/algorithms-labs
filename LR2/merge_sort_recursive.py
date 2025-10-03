def merge(left, right):
    merged, comparisons, assignments = [], 0, 0
    i = j = 0
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
        assignments += 1
    while i < len(left):
        merged.append(left[i]); i += 1
        assignments += 1
    while j < len(right):
        merged.append(right[j]); j += 1
        assignments += 1
    return merged, comparisons, assignments


def merge_sort_recursive(arr):
    comparisons = assignments = 0
    recursive_calls = 0

    if len(arr) <= 1:
        return arr[:], comparisons, assignments, recursive_calls

    mid = len(arr) // 2
    assignments += 1

    recursive_calls += 2
    left,  c1, a1, r1 = merge_sort_recursive(arr[:mid])
    right, c2, a2, r2 = merge_sort_recursive(arr[mid:])
    comparisons += c1 + c2
    assignments += a1 + a2
    recursive_calls += r1 + r2

    merged, cM, aM = merge(left, right)
    return merged, comparisons + cM, assignments + aM, recursive_calls


if __name__ == "__main__":
    my_list = [47, 50, 61, 41, 53, 12, 68, 63, 3]  
    sorted_list, comps, assigns, rcalls = merge_sort_recursive(my_list)
    print("Оригінальний список:", my_list)
    print("Відсортований список:", sorted_list)
    print(f"Загальна кількість порівнянь: {comps}")
    print(f"Загальна кількість присвоювань: {assigns}")
    print(f"Загальна кількість рекурсивних викликів: {rcalls}")

