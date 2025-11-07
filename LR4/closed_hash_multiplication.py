from math import sqrt, floor

WORDS = ["Не","той","багатий","у","кого","багато","грошей",
         "а","той","у","кого","душа","багата"]

ALPHABET = ["А","Б","В","Г","Ґ","Д","Е","Є","Ж","З","И","І","Ї","Й",
            "К","Л","М","Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч",
            "Ш","Щ","Ь","Ю","Я"]
POS = {ch: i+1 for i, ch in enumerate(ALPHABET)}
POS.update({ch.lower(): i+1 for i, ch in enumerate(ALPHABET)})

M = 16
A = (sqrt(5) - 1) / 2  # ≈ 0.6180339887


def ksum(w: str) -> int:
    return sum(POS.get(ch, 0) for ch in w)


def h_mul(w: str, m: int = M, a: float = A) -> int:
    frac = (ksum(w) * a) % 1
    return floor(m * frac)


def build_closed_linear(words, m: int = M, h=h_mul):
    """Побудова таблиці (лінійне зондування)."""
    table = [None] * m
    for w in words:
        start = h(w, m)
        for i in range(m):
            idx = (start + i) % m
            if table[idx] is None:
                table[idx] = w
                break
    return table


def print_table(t):
    print("\n--- Хеш-таблиця (Відкрита адресація, метод множення, M=16) ---")
    print("Індекс | Слово")
    print("-------|-------")
    for i, x in enumerate(t):
        print(f"{i:02d}     | {x if x is not None else '(NULL)'}")


def comparisons_for_success(table, word, m: int = M, h=h_mul) -> int:
    """
    К-сть порівнянь під час успішного пошуку елемента.
    (Рівно стільки ж для видалення, бо спочатку треба знайти.)
    """
    start = h(word, m)
    comps = 0
    for i in range(m):
        idx = (start + i) % m
        comps += 1
        if table[idx] == word:         
            return comps
        if table[idx] is None:        
            return comps
    return comps


def evaluate_average_and_max(table, words):
    per_word = []
    total = 0
    max_comp, max_word = -1, None
    for w in words:          
        c = comparisons_for_success(table, w)
        per_word.append((w, c))
        total += c
        if c > max_comp:
            max_comp, max_word = c, w
    avg = total / len(words)
    return per_word, avg, max_comp, max_word


if __name__ == "__main__":
    table = build_closed_linear(WORDS, M, h_mul)
    print_table(table)

    per_word, avg, max_comp, max_word = evaluate_average_and_max(table, WORDS)

    print("\n--- Оцінка ефективності пошуку/видалення (успішні пошуки) ---")
    for w, c in per_word:
        print(f"{w:<7} -> порівнянь: {c}")

    print(f"\nСередня кількість порівнянь: {avg:.2f}")
    print(f"Максимальна кількість порівнянь: {max_comp} (елемент: «{max_word}»)")

