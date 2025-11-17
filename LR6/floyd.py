INF = float('inf')

W = [
    [0,   4,   1,   4,   INF, INF, INF, INF],
    [4,   0,   5,   INF, 7,   3,   INF, INF],
    [1,   5,   0,   5,   INF, 5,   INF, 4  ],
    [4,   INF, 5,   0,   1,   INF, INF, INF],
    [INF, 7,   INF, 1,   0,   INF, 4,   INF],
    [INF, 3,   5,   INF, INF, 0,   6,   INF],
    [INF, INF, INF, INF, 4,   6,   0,   5  ],
    [INF, INF, 4,   INF, INF, INF,   5,   0  ]
]


def floyd_warshall(W):
    """Реалізація алгоритму Флойда–Уоршелла.
    На вхід подається матриця ваг W, на вихід — матриця найкоротших відстаней D.
    """
    n = len(W)
    dist = [row[:] for row in W]

    # Основні три вкладені цикли алгоритму Флойда
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Якщо шлях i -> k -> j коротший, ніж поточний i -> j — оновлюємо
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def print_matrix(D):
    """Допоміжна функція для красивого виводу матриці відстаней."""
    n = len(D)
    print("Матриця найкоротших відстаней D (рядки/стовпці відповідають вершинам 1..8):")
    for i in range(n):
        row_str = " ".join(f"{D[i][j]:2d}" for j in range(n))
        print(row_str)


if __name__ == "__main__":
    D = floyd_warshall(W)
    print_matrix(D)

