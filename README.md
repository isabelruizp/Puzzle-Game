This project is a web-based 8-puzzle game built with Streamlit. Users can upload any image, which is then split into 9 tiles to create a playable 3x3 puzzle. The application allows:
Uploading a custom image.
Shuffling into a solvable puzzle.
Solving the puzzle using the A★ (A-star) algorithm.
Viewing each step toward the optimal solution.

Algorithm Details:
The core solving logic uses the A★ algorithm with the Manhattan Distance heuristic, which calculates the total number of moves each tile is away from its goal position. This is an admissible and consistent heuristic ideal for grid-based puzzles.

Manhattan Distance is used to reflects the true minimal number of moves without considering diagonal shortcuts, making it accurate, fast and efficient.

To run the application:
Install required packages: pip install -r requirements.txt
Then run the command: streamlit run app.py
This will open a local web app in your browser

Project Structure:
8_puzzle_solver/
├── app.py                  # Main Streamlit UI
├── state.py                # Puzzle logic and heuristics
├── heuristicseach.py         # A★ search implementation
├── utils.py                # Image splitting and reassembly
├── requirements.txt        # Python package list
└── README.pdf              # This file

Features:
Visual puzzle interaction
Solvability check on shuffle
Optimal solution steps with move-by-move preview
Node exploration and solve time metrics

Isabel Ruiz
iruiz053@fiu.edu
PID: 6353644
Artificial Intelligence# Puzzle-Game
Puzzle Game using A* and Heuristic Search
