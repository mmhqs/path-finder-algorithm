## 💻 The algorithm

The A* algorithm is a landmark in artificial intelligence and graph theory. The **A* Algorithm** was developed in 1968 by Peter Hart, Nils Nilsson, and Bertram Raphael. It is an extension of Dijkstra's Algorithm that uses a heuristic to improve performance. The Manhattan Heuristic is used in grid-based environments (like mazes) where movement is restricted to orthogonal directions (no diagonals).

The set of functions presented in this repo implements the **A* Search Algorithm (A-Star)** to find the shortest path between a start point ('S') and an end point ('E') in a 2D maze represented by a grid (matrix).

A* is a graph search algorithm that finds the path with the lowest cost by combining the actual cost traveled so far (**g(n)**) with an estimated cost remaining to the goal (heuristic, **h(n)**). The total cost function (**f(n)**) is given by:

`f(n) = g(n) + h(n)`

Maze components:

Symbol | Meaning | Type
--------| ----------- | -----
'S'	| Start Point | 	Traversable
'E' | 	End Point (Goal) | 	Traversable
'0' | Free Cell (walkable)	 | Traversable
'1' | Obstacle (wall, not walkable)	 | Blocked
'P' | Found Path Point (after solution)	 | Traversable
'.' | Free Cell in final result (for visualization) | 	Traversable
'#' | Obstacle in final result (for visualization) | 	Blocked

---

## 🛠️ Algorithm Implementation Details
This is the main function that executes the A* search: `astar(grid, start, end)`

Data Structures:
- `open_set` (Min Heap)`: a priority queue implemented with heapq, which stores the cells to be explored. Priority is given by the $f(n)$ value (estimated total cost), ensuring the most promising node is always retrieved first (heappop).
- `g_score` (Dictionary): stores the actual cost ($g(n)$) from the start point to each cell.
- `came_from` (Dictionary): used for path tracking. Stores the neighbor from which each cell was reached (necessary for path reconstruction).
- `closed` (Set): stores nodes that have been fully evaluated.

Heuristic Used: the `manhattan_distance(a, b)` function calculates the Manhattan distance. This is an admissible heuristic (it never overestimates the actual cost), ensuring the A* algorithm finds the shortest/optimal path.

Helper Functions
- `read_maze(lines)`: processes the text input (lines) and transforms it into a grid matrix. Identifies and stores the coordinates of the 'S' (Start) and 'E' (End) points. Replaces 'S' and 'E' with '0' in the grid so the search algorithm can traverse them.
- `neighbors(position, rows, cols)`: generates the coordinates of valid neighbors (up, down, left, right) for a given position, ensuring they are within the grid boundaries.
- `reconstruct_path(came_from, current)`: after A* finds the goal, this function uses the `came_from` dictionary to backtrack the path, from the end point back to the start.
- `highlight_path(grid, start, end, path)`: creates a visual representation of the maze with the found path, marking it with 'P'.