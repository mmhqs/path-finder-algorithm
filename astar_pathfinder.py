from heapq import heappop, heappush


def read_maze(lines):
    """Transforma linhas em matriz e identifica os pontos S e E."""
    grid = []
    start = None
    end = None

    for row_index, raw_line in enumerate(lines):
        tokens = list(raw_line.strip())
        row = []
        for col_index, value in enumerate(tokens):
            if value == "S":
                start = (row_index, col_index)
                row.append("0")
            elif value == "E":
                end = (row_index, col_index)
                row.append("0")
            elif value in ("0", "1"):
                row.append(value)
            else:
                raise ValueError(f"Valor inválido no labirinto: {value!r}")
        grid.append(row)

    if start is None or end is None:
        raise ValueError("Labirinto deve conter os pontos S e E.")

    return grid, start, end


def manhattan_distance(a, b):
    """Heurística que estima a distância usando a distância de Manhattan."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def neighbors(position, rows, cols):
    """Retorna as posições vizinhas (cima, baixo, esquerda, direita)."""
    row, col = position
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for d_row, d_col in moves:
        next_row = row + d_row
        next_col = col + d_col
        if 0 <= next_row < rows and 0 <= next_col < cols:
            yield next_row, next_col


def reconstruct_path(came_from, current):
    """Reconstrói o caminho do objetivo até o início."""
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def astar(grid, start, end):
    """Executa o algoritmo A* em um labirinto 2D."""
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    open_set = []
    heappush(open_set, (0 + manhattan_distance(start, end), 0, start))

    came_from = {}
    g_score = {start: 0}
    closed = set()

    while open_set:
        _, current_cost, current = heappop(open_set)

        if current in closed:
            continue

        if current == end:
            return reconstruct_path(came_from, current)

        closed.add(current)

        for next_position in neighbors(current, rows, cols):
            row, col = next_position
            if grid[row][col] == "1":
                continue

            tentative_cost = current_cost + 1
            if tentative_cost < g_score.get(next_position, float("inf")):
                came_from[next_position] = current
                g_score[next_position] = tentative_cost
                priority = tentative_cost + manhattan_distance(next_position, end)
                heappush(open_set, (priority, tentative_cost, next_position))

    return None


def highlight_path(grid, start, end, path):
    """Cria uma cópia do labirinto com o caminho marcado."""
    marked = [row[:] for row in grid]

    for row, col in path:
        if (row, col) == start:
            marked[row][col] = "S"
        elif (row, col) == end:
            marked[row][col] = "E"
        else:
            marked[row][col] = "P"

    # Garante que obstáculos continuem visíveis.
    for row in range(len(marked)):
        for col in range(len(marked[row])):
            if marked[row][col] == "0":
                marked[row][col] = "."
            elif marked[row][col] == "1":
                marked[row][col] = "#"

    return marked


def main():
    # Labirinto de exemplo 20x20 com um caminho claro de S até E.
    lines = [
        "S0000011111111111111",
        "11111011111111111111",
        "11111011111111111111",
        "11111011111111111111",
        "11111011111111111111",
        "11111011111111111111",
        "11111011111111111111",
        "11111011111111111111",
        "11111011111111111111",
        "11111011111111111111",
        "11111000000000001111",
        "11111111111111101111",
        "11111111111111101111",
        "11111111111111101111",
        "11111111111111101111",
        "11111111111111101111",
        "11111111111111101111",
        "11111111111111101111",
        "11111111111111101111",
        "1111111111111110000E",
    ]

    grid, start, end = read_maze(lines)
    path = astar(grid, start, end)

    if path is None:
        print("Nenhum caminho encontrado.")
        return

    print("Caminho encontrado (linha, coluna):")
    for step in path:
        print(step)

    print("\nLabirinto com caminho:")
    marked = highlight_path(grid, start, end, path)
    for row in marked:
        print(" ".join(row))


if __name__ == "__main__":
    main()
