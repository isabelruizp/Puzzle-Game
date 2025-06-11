
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)

MOVES = {
    0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
    3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
    6: [3, 7], 7: [4, 6, 8], 8: [5, 7]
}

class PuzzleState:
    def __init__(self, board, g=0, parent=None):
        self.board = board
        self.g = g
        self.parent = parent
        self.h = self.manhattan()
        self.f = self.g + self.h

    def manhattan(self):
        dist = 0
        for idx, value in enumerate(self.board):
            if value == 0:
                continue
            cur_row, cur_col = divmod(idx, 3)
            goal_row, goal_col = divmod(value - 1, 3)
            dist += abs(cur_row - goal_row) + abs(cur_col - goal_col)
        return dist

    def is_goal(self):
        return self.board == GOAL_STATE

    def get_neighbors(self):
        zero_idx = self.board.index(0)
        neighbors = []
        for swap_with in MOVES[zero_idx]:
            new_board = list(self.board)
            new_board[zero_idx], new_board[swap_with] = new_board[swap_with], new_board[zero_idx]
            neighbor = PuzzleState(tuple(new_board), g=self.g + 1, parent=self)
            neighbors.append(neighbor)
        return neighbors

    @staticmethod
    def is_solvable(board):
        inv_count = 0
        arr = [x for x in board if x != 0]
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    inv_count += 1
        return (inv_count % 2) == 0

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return isinstance(other, PuzzleState) and self.board == other.board

    def __hash__(self):
        return hash(self.board)

    def reconstruct_path(self):
        path = []
        node = self
        while node:
            path.append(node)
            node = node.parent
        return list(reversed(path))
