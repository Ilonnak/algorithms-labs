import math

# Константи
M = 16
A = 0.618

# Список вхідних слів
WORDS = ["Не", "той", "багатий", "у", "кого", "багато", "грошей",
         "а", "той", "у", "кого", "душа", "багата"]

# Словник позицій українських літер
ALPHABET = [
    "А","Б","В","Г","Ґ","Д","Е","Є","Ж","З","И","І","Ї","Й","К","Л","М",
    "Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ","Ь","Ю","Я"
]
LETTER_POSITIONS = {ch: i+1 for i, ch in enumerate(ALPHABET)}
LETTER_POSITIONS.update({ch.lower(): i+1 for i, ch in enumerate(ALPHABET)})

def key_value(word: str) -> int:
    """Обчислює K як суму позицій літер у слові."""
    return sum(LETTER_POSITIONS.get(ch, 0) for ch in word)

def hash_multiplication(k: int, m: int = M, a: float = A) -> int:
    """Хеш-функція за методом множення."""
    fractional = (k * a) % 1
    return math.floor(m * fractional)

def build_open_hash_table(words: list, m: int) -> list:
    """Будує хеш-таблицю з ланцюжками (списками)."""
    hash_table = [[] for _ in range(m)]
    for word in words:
        k = key_value(word)
        address = hash_multiplication(k, m)
        hash_table[address].append(word)
    return hash_table

def display_hash_table(table: list):
    """Виводить хеш-таблицю у зручному форматі."""
    print("\n--- Результат хешування (метод множення, M=16) ---")
    for i, chain in enumerate(table):
        print(f"Індекс {i:02d}: {chain}")

# ===== ПІДРАХУНОК ПОРІВНЯНЬ =====
def count_success_searches(words: list, table: list) -> None:
    """
    Оцінка ефективності пошуку/видалення (успішні пошуки):
    для кожного слова рахується кількість порівнянь у своєму ланцюжку.
    """
    print("\n--- Оцінка ефективності пошуку/видалення (успішні пошуки) ---")
    cmp_counts = []
    max_cmp, max_elem = -1, None

    for w in words:
        k = key_value(w)
        b = hash_multiplication(k, M, A)
        chain = table[b]
        comps = 0
        for item in chain:
            comps += 1
            if item == w:
                break
        cmp_counts.append(comps)
        print(f"{w:<7} -> порівнянь: {comps}")
        if comps > max_cmp:
            max_cmp, max_elem = comps, w

    avg_cmp = sum(cmp_counts) / len(cmp_counts)
    print(f"\nСередня кількість порівнянь: {avg_cmp:.2f}")
    print(f"Максимальна кількість порівнянь: {max_cmp} (елемент: «{max_elem}»)")
    print("Примітка: для видалення вартість дорівнює вартості успішного пошуку.")

# ===== Виконання =====
if __name__ == "__main__":
    hash_table = build_open_hash_table(WORDS, M)
    display_hash_table(hash_table)
    count_success_searches(WORDS, hash_table)

