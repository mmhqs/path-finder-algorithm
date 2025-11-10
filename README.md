# Maze path finder algorithm
This repo presents a Python implementation of the algorithm to find the shortest path in a given maze. 

<img src="docs/images/labyrinth.PNG" alt="Maze" width="300">

[1. Understanding the algorithm](#understanding-the-algorithm)

[2. How to run the project in Python 🐍](#how-to-run-the-project-in-python)

[3. Algorithm analysis](#algorithm-analysis)

## Understanding the algorithm
To understand the algorithm, I did some studying and compiled my research in the [study](docs/study.md) file.

After studying the algorithm a little, I implemented the algorithm in Python. I also **added comments to the code** to make it easier to understand each step of the algorithm.

---

## How to run the project in Python 🐍
The algorithm to find the Hamiltonian path in a graph, implemented in Python, can be found in [astar_pathfinder.py](code/astar_pathfinder.py) file. You can download it if you want to run it on your computer.

This guide assumes you already have Python installed on your computer, ok? ✅

### Step 1: open your terminal 🖥️
First, you need to open a command-line interface.

### Step 2: navigate to the correct folder 📂
You must tell the terminal where your `astar_pathfinder.py` file is located. You'll use the `cd` (change directory) command for this. Find the path to the folder containing the `astar_pathfinder.py` file you downloaded from this repo.

Type cd followed by a space and the path to your folder. Example:

`cd Folder1/Folder2/Folder3/MyProject`

### Step 3: run the file ▶️
Once you are in the correct folder, you can run the Python script. Type python followed by the name of your file. Example:

`python astar_pathfinder.py`

## 🧩 Extra Feature: Diagonal Movement

In addition to the basic A* algorithm implementation, we developed an extended version that allows the robot to move in diagonal directions, with a movement cost of √2.

### Implementation File

- **Code:** [`astar_with_diagonals.py`](code/astar_with_diagonals.py)

### Additional Features

- Movement in 8 directions (including diagonals)
- Differentiated movement costs:
  - Horizontal/vertical movements: cost 1
  - Diagonal movements: cost √2 (approximately 1.414)
- **Chebyshev distance heuristic**: Optimized for 8-direction movement
- Corner-cutting prevention: diagonal moves only allowed when adjacent cells are free

### How to Use

1. Run the `astar_with_diagonals.py` file:
```bash
python astar_with_diagonals.py
```

### Sample Output (Open Maze)

```
=== A* Algorithm with Diagonal Movements ===
Cost: Cardinal movements = 1, Diagonal movements = √2 ≈ 1.414
Heuristic: Chebyshev Distance (ideal for 8 directions)

Path found (row, column):
 1. (0, 0)
 2. (1, 1)
 3. (2, 2)
 4. (3, 3)
 5. (4, 4)
     ...
16. (15, 15)
17. (16, 16)
18. (17, 17)
19. (18, 18)
20. (19, 19)

Path length: 20 steps
Total path cost: 26.870
Diagonal moves: 19
Cardinal moves: 0
```

### Key Improvements

1. **Chebyshev Heuristic**: `max(|dx|, |dy|)` - perfect for 8-direction movement
2. **Optimal Path Finding**: Finds the shortest possible path in open areas
3. **Cost Efficiency**: Reduces both path length and total cost

### Performance Comparison

| Scenario | Basic A* | A* with Diagonals | Improvement |
|----------|----------|-------------------|-------------|
| **Open Area (20x20)** | 38 steps | 20 steps | **-47.4%** |
| Narrow Corridors | Minimal improvement | Minimal improvement | - |
| Mixed Environment | Moderate improvement | Significant improvement | **-20% to -40%** |

### Technical Details

- **Heuristic**: Chebyshev distance ensures optimality with diagonal moves
- **Cost Calculation**: Accurate √2 cost for diagonals, 1 for cardinals
- **Path Validation**: Prevents corner-cutting in diagonal movements
- **Performance**: Maintains O(n log n) complexity with efficient priority queue

### Advantages

- **Shorter paths** in open environments
- **More natural movement** patterns
- **Better performance** in games and robotics applications
- **Maintains optimality** with admissible heuristic

---