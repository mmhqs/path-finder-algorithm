from heapq import heappop, heappush
import math


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


def chebyshev_distance(a, b):
    """Heurística ideal para movimentos em 8 direções (diagonais)."""
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


def neighbors_with_diagonals(position, rows, cols):
    """Retorna as posições vizinhas (8 direções: cima, baixo, esquerda, direita + diagonais)."""
    row, col = position
    moves = [
        (-1, 0), (1, 0), (0, -1), (0, 1),      # Movimentos cardinais (custo 1)
        (-1, -1), (-1, 1), (1, -1), (1, 1)     # Movimentos diagonais (custo √2)
    ]
    
    for d_row, d_col in moves:
        next_row = row + d_row
        next_col = col + d_col
        if 0 <= next_row < rows and 0 <= next_col < cols:
            yield (next_row, next_col), (d_row, d_col)


def get_move_cost(move):
    """Retorna o custo do movimento: 1 para cardinais, √2 para diagonais."""
    d_row, d_col = move
    # Se ambos os componentes são não-zero, é um movimento diagonal
    if d_row != 0 and d_col != 0:
        return math.sqrt(2)  # Custo √2 para diagonais
    else:
        return 1.0  # Custo 1 para movimentos cardinais


def can_move_diagonally(grid, current, move):
    """Verifica se um movimento diagonal é possível sem cortar cantos."""
    row, col = current
    d_row, d_col = move
    
    # Para movimento diagonal, verifica se ambas as células adjacentes estão livres
    if grid[row + d_row][col] == "1":  # Verifica movimento vertical
        return False
    if grid[row][col + d_col] == "1":  # Verifica movimento horizontal
        return False
    return True


def reconstruct_path(came_from, current):
    """Reconstrói o caminho do objetivo até o início."""
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def astar_with_diagonals(grid, start, end):
    """Executa o algoritmo A* em um labirinto 2D com movimentos diagonais."""
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    open_set = []
    initial_heuristic = chebyshev_distance(start, end)
    heappush(open_set, (initial_heuristic, 0, start))

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

        for next_position, move in neighbors_with_diagonals(current, rows, cols):
            row, col = next_position
            
            # Verifica se a célula destino é um obstáculo
            if grid[row][col] == "1":
                continue

            # Para movimentos diagonais, verifica se pode mover sem cortar cantos
            move_cost = get_move_cost(move)
            if move_cost > 1:  # É movimento diagonal
                if not can_move_diagonally(grid, current, move):
                    continue

            tentative_cost = current_cost + move_cost
            
            # Se encontrou um caminho melhor para este vizinho
            if tentative_cost < g_score.get(next_position, float("inf")):
                came_from[next_position] = current
                g_score[next_position] = tentative_cost
                heuristic = chebyshev_distance(next_position, end)
                priority = tentative_cost + heuristic
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


def calculate_path_cost(path):
    """Calcula o custo total do caminho considerando movimentos diagonais."""
    total_cost = 0
    for i in range(len(path) - 1):
        current = path[i]
        next_pos = path[i + 1]
        d_row = next_pos[0] - current[0]
        d_col = next_pos[1] - current[1]
        if d_row != 0 and d_col != 0:
            total_cost += math.sqrt(2)
        else:
            total_cost += 1
    return total_cost


def main():
    print("=== Algoritmo A* com Movimentos Diagonais ===")
    print("Custo: Movimentos cardinais = 1, Movimentos diagonais = √2 ≈ 1.414")
    print("Heurística: Distância de Chebyshev (ideal para 8 direções)\n")
    
    # Labirinto otimizado para diagonais
    lines = [
        "S0000000000000000000",
        "00000000000000000000",
        "00000000000000000000", 
        "00000000000000000000",
        "00000000000000000000",
        "00000000000000000000",
        "00000000000000000000",
        "00000000000000000000",
        "00000000000000000000",
        "00000000000000000000",
        "00000000000000000000",
        "00000000000000000000",
        "00000000000000000000",
        "00000000000000000000",
        "00000000000000000000",
        "00000000000000000000",
        "00000000000000000000",
        "00000000000000000000",
        "00000000000000000000",
        "0000000000000000000E",
    ]

    print("Labirinto de teste (aberto, ideal para diagonais):")
    for line in lines:
        print(line)
    print()
    
    grid, start, end = read_maze(lines)
    path = astar_with_diagonals(grid, start, end)

    if path is None:
        print("Nenhum caminho encontrado.")
        return

    print("Caminho encontrado (linha, coluna):")
    # Mostrar apenas os primeiros e últimos passos para não poluir a tela
    for i in range(min(5, len(path))):
        print(f"{i+1:2d}. {path[i]}")
    if len(path) > 10:
        print("     ...")
        for i in range(len(path)-5, len(path)):
            print(f"{i+1:2d}. {path[i]}")

    print(f"\nComprimento do caminho: {len(path)} passos")
    
    # Calcula custo total do caminho
    total_cost = calculate_path_cost(path)
    print(f"Custo total do caminho: {total_cost:.3f}")

    # Conta movimentos diagonais
    diagonal_moves = 0
    for i in range(len(path) - 1):
        current = path[i]
        next_pos = path[i + 1]
        d_row = next_pos[0] - current[0]
        d_col = next_pos[1] - current[1]
        if d_row != 0 and d_col != 0:
            diagonal_moves += 1
    
    print(f"Movimentos diagonais: {diagonal_moves}")
    print(f"Movimentos cardinais: {len(path) - 1 - diagonal_moves}")

    print("\nLabirinto com caminho (P = caminho, . = livre):")
    marked = highlight_path(grid, start, end, path)
    # Mostrar apenas uma parte do labirinto para visualização
    for i in range(min(10, len(marked))):
        print(" ".join(marked[i][:20]))


if __name__ == "__main__":
    main()