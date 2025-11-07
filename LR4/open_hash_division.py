M = 13

WORDS = ["Не", "той", "багатий", "у", "кого", "багато", "грошей",
         "а", "той", "у", "кого", "душа", "багата"]

ALPHABET = [
    "А","Б","В","Г","Ґ","Д","Е","Є","Ж","З","И","І","Ї","Й","К","Л","М",
    "Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ","Ь","Ю","Я"
]
LETTER_POSITIONS = {ch: i+1 for i, ch in enumerate(ALPHABET)}
LETTER_POSITIONS.update({ch.lower(): i+1 for i, ch in enumerate(ALPHABET)})

def simple_hash_from_map(key: str) -> int:
    """h(k) = (сума позицій букв) mod M."""
    s = 0
    for ch in key:
        s += LETTER_POSITIONS.get(ch, 0)
    return s % M

def build_open_hash_table(words: list, m: int) -> list:
    """Таблиця з ланцюжками (списками)."""
    table = [[] for _ in range(m)]
    for w in words:
        table[simple_hash_from_map(w)].append(w)
    return table

def count_success_searches(words: list, table: list) -> None:
    """
    Оцінка ефективності пошуку/видалення (успішні пошуки):
    для кожного слова рахуємо кількість порівнянь у його бакеті.
    """
    print("\n--- Оцінка ефективності пошуку/видалення (успішні пошуки) ---")
    cmp_counts = []
    max_cmp, max_elem = -1, None

    for w in words:
        b = simple_hash_from_map(w)
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

def display_hash_table(table: list):
    print("\n--- Результат хешування (метод ділення, M=13) ---")
    for i, chain in enumerate(table):
        print(f"Індекс {i:02d}: {chain}")

if __name__ == "__main__":
    ht = build_open_hash_table(WORDS, M)
    display_hash_table(ht)
    count_success_searches(WORDS, ht)

