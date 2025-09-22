def selection_sort_trace(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0
    print("Початковий масив:", arr)
    print("-" * 30)

    for i in range(n - 1):
        min_index = i
        assignments += 1
        print(f"Ітерація {i}:")
        print(f"  Поточний елемент (для обміну): arr[{i}] = {arr[i]}")
        print(f"  Шукаємо мінімальний елемент у частині: {arr[i:]}")

        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
                assignments += 1

        print(f"  Знайдено мінімальний елемент: arr[{min_index}] = {arr[min_index]}")
        comparisons += 1
        if min_index != i:
            left, right = arr[i], arr[min_index]
            arr[i], arr[min_index] = arr[min_index], arr[i]
            assignments += 3
            print(f"  Обмін arr[{i}] ({left}) і arr[{min_index}] ({right})")

        print(f"  Масив після ітерації {i}: {arr}")
        print("-" * 30)

    print("Сортування завершено.")
    print("Фінальний відсортований масив:", arr)
    print(f"Загальна кількість порівнянь: {comparisons}")
    print(f"Загальна кількість присвоєнь: {assignments}")

data = [53, 100, 44, 74, 53, 38, 82, 65, 28]
selection_sort_trace(data.copy())
