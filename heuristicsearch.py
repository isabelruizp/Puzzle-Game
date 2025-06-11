
import heapq
import time
from state import PuzzleState

def a_star(start_state):
    start_time = time.time()
    open_set = []
    heapq.heappush(open_set, start_state)
    g_score = {start_state: 0}
    closed_set = set()
    nodes_expanded = 0

    while open_set:
        current = heapq.heappop(open_set)
        nodes_expanded += 1

        if current.is_goal():
            return {
                "success": True,
                "path": current.reconstruct_path(),
                "nodes_expanded": nodes_expanded,
                "time": time.time() - start_time
            }

        closed_set.add(current)
        for neighbor in current.get_neighbors():
            if neighbor in closed_set:
                continue
            tentative_g = current.g + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                neighbor.g = tentative_g
                neighbor.h = neighbor.manhattan()
                neighbor.f = neighbor.g + neighbor.h
                neighbor.parent = current
                g_score[neighbor] = tentative_g
                heapq.heappush(open_set, neighbor)

    return {
        "success": False,
        "path": [],
        "nodes_expanded": nodes_expanded,
        "time": time.time() - start_time
    }


