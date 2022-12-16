from typing import List, Tuple

class Computer:
    def __init__(self, num: int):
        self.num = num
        self.connections = []
        
    def add_connection(self, other: 'Computer', cost: int):
        self.connections.append((other, cost))
        

def find_min_cost(n: int, p: int, k: int, connections: List[Tuple[int, int, int]]) -> int:
    computers = {num: Computer(num) for num in range(1, n+1)}
    for a, b, cost in connections:
        computers[a].add_connection(computers[b], cost)
        computers[b].add_connection(computers[a], cost)
    
    queue = [(0, k, computers[1])]
    visited = set()
    
    while queue:
        cost, free_connections, node = heapq.heappop(queue)
        
        if node in visited:
            continue
        visited.add(node)
        
        if node.num == n:
            return cost
