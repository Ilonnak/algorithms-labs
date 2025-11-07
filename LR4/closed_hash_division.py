M = 13

WORDS = [
    "Не", "той", "багатий", "у", "кого", "багато",
    "грошей", "а", "той", "у", "кого", "душа", "багата"
]

ALPHABET = [
    "А","Б","В","Г","Ґ","Д","Е","Є","Ж","З","И","І","Ї","Й",
    "К","Л","М","Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч",
    "Ш","Щ","Ь","Ю","Я"
]
LETTER_POSITIONS = {ch: i+1 for i, ch in enumerate(ALPHABET)}
LETTER_POSITIONS.update({ch.lower(): i+1 for i, ch in enumerate(ALPHABET)})

def key_sum(word: str) -> int:
    """Сума позицій літер слова в укр. алфавіті."""
    return sum(LETTER_POSITIONS.get(ch, 0) for ch in word)

def primary_hash(word: str, m: int = M) -> int:
    """Первинна хеш-функція (метод ділення): h(k) = K mod m."""
    return key_sum(word) % m

def build_closed_hash_table(words: list, m: int = M) -> list:
    """
    Будує закриту хеш-таблицю з відкритою адресацією (лінійне зондування).
    """
    table = [None] * m
    for w in words:
        start = primary_hash(w, m)
        for i in range(m):
            idx = (start + i) % m
            if table[idx] is None:
                table[idx] = w
                break
        else:
            raise RuntimeError(f"Переповнення таблиці: не вдалося вставити «{w}»")
    return table

def successful_search_comparisons(word: str, table: list, m: int = M) -> int:
    """
    Повертає кількість порівнянь під час УСПІШНОГО пошуку слова у таблиці.
    Для закритої адресації (лінійне зондування) — це рівно стільки ж,
    скільки й для видалення (бо спочатку треба знайти).
    """
    start = primary_hash(word, m)
    comparisons = 0
    for i in range(m):
        idx = (start + i) % m
        comparisons += 1                  
        cell = table[idx]
        if cell is None:                     
            return comparisons
        if cell == word:
            return comparisons
    return comparisons  

def per_word_costs(words: list, table: list, m: int = M) -> list[tuple[str, int]]:
    """Список пар (слово, #порівнянь) для успішного пошуку кожного слова."""
    return [(w, successful_search_comparisons(w, table, m)) for w in words]

def average_comparisons(words: list, table: list, m: int = M) -> float:
    """Середня кількість порівнянь для успішного пошуку/видалення."""
    costs = [c for _, c in per_word_costs(words, table, m)]
    return sum(costs) / len(costs)

def argmax_cost(words: list, table: list, m: int = M) -> tuple[str, int]:
    """
    Елемент із максимальною кількістю порівнянь і його вартість.
    Якщо кілька — поверне перший з макс. значенням.
    """
    costs = per_word_costs(words, table, m)
    return max(costs, key=lambda p: p[1])

def display_hash_table(table: list):
    """Вивід у форматі для таблиці результатів."""
    print("\n--- Хеш-таблиця (Відкрита адресація, метод ділення, M=13) ---")
    print("Індекс | Слово")
    print("-------|-------")
    for i, item in enumerate(table):
        print(f"{i:02d}     | {item if item is not None else '(NULL)'}")

def display_metrics(words: list, table: list, m: int = M):
    print("\n--- Оцінка ефективності пошуку/видалення (успішні пошуки) ---")
    for w, c in per_word_costs(words, table, m):
        print(f"{w:>7}  -> порівнянь: {c}")
    avg = average_comparisons(words, table, m)
    worst_word, worst_cost = argmax_cost(words, table, m)
    print(f"\nСередня кількість порівнянь: {avg:.2f}")
    print(f"Максимальна кількість порівнянь: {worst_cost} (елемент: «{worst_word}»)")

if __name__ == "__main__":
    ht = build_closed_hash_table(WORDS, M)
    display_hash_table(ht)
    display_metrics(WORDS, ht, M)

