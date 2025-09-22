def insertion_sort_trace(arr):
    n = len(arr)
    print("Початковий масив:", arr)
    print("-" * 30)
    for i in range(1, n):
        key = arr[i]
        print(f"Ітерація {i}:")
        print(f"  Елемент для вставки (key): {key}")
        print(f"  Відсортована частина: {arr[:i]}")
        j = i - 1
        # показуємо всі порівняння й зсуви
        while j >= 0 and arr[j] > key:
            print(f"  Порівняння: {arr[j]} > {key} — True. Зсуваємо {arr[j]} вправо.")
            arr[j + 1] = arr[j]
            j -= 1
        if j >= 0:
            print(f"  Порівняння: {arr[j]} > {key} — False. Цикл завершено.")
        print(f"  Вставка {key} на позицію {j + 1}.")
        arr[j + 1] = key
        print(f"  Масив після ітерації {i}: {arr}")
        print("-" * 30)
    print("Сортування завершено.")
    print("Фінальний відсортований масив:", arr)
data = [53, 100, 44, 74, 53, 38, 82, 65, 28]

print("=== Трасування Insertion Sort ===")
insertion_sort_trace(data)
