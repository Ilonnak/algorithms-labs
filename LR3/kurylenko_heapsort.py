# Лічильники
comparisons = 0   # кількість порівнянь між елементами масиву
assignments = 0   # кількість присвоювань під час обмінів (swap)

def swap(arr, i, j):
    global assignments
    arr[i], arr[j] = arr[j], arr[i]
    assignments += 3  # один обмін = 3 присвоювання

def sink(arr, i, n):
    global comparisons
    k = i
    while True:
        j = 2 * k + 1
        if j >= n:
            break
        # порівняння дітей між собою
        if j + 1 < n:
            comparisons += 1                # arr[j + 1] > arr[j]
            if arr[j + 1] > arr[j]:
                j += 1
        # порівняння батька з найбільшим із дітей
        comparisons += 1                    # arr[k] >= arr[j]
        if arr[k] >= arr[j]:
            break
        swap(arr, k, j)
        k = j

def heapsort(arr):
    n = len(arr)
    print("Початковий масив:", arr)

    print("\n--- Фаза 1: Побудова максимальної купи ---")
    for i in range(n // 2 - 1, -1, -1):
        print(f"Занурюється елемент з індексу {i}: {arr[i]}")
        sink(arr, i, n)

    print("\nМасив після побудови купи:", arr)

    print("\n--- Фаза 2: Сортування ---")
    for i in range(n - 1, 0, -1):
        print(f"Обмінюємо корінь ({arr[0]}) і елемент ({arr[i]})")
        swap(arr, 0, i)
        n -= 1
        print(f"Розмір купи тепер {n}")
        sink(arr, 0, n)
        print("Масив на поточному кроці:", arr)

    return arr

A = [47, 50, 61, 41, 53, 12, 68, 63, 3]
sorted_A = heapsort(A)
print("\nВідсортований масив:", sorted_A)

# Підсумки для Таблиці 3.4
print(f"\nКількість порівнянь (елемент-елемент): {comparisons}")
print(f"Кількість присвоювань (через swap): {assignments}")

