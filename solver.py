# Paste your personal matrix instead of the one below
matrix = [[8, 8, 8, 8, "Z", 9, 7, 7, 8, 9],
          [8, 8, 6, 7, "Z", 9, 9, 9, 9, 9],
          [9, 9, 9, 9, "Z", 9, 9, 9, 9, 9],
          [9, "Z", "Z", "Z", "Z", "Z", "Z", "Z", 9, 7],
          [9, "Z", 6, 2, "Z", 8, 9, 9, 9, 6],
          [9, "Z", 5, 4, "Z", 3, 3, 3, 3, 3],
          [3, 3, 3, 3, 3, 9, 4, "Z", 9, 7],
          [9, 9, 8, 8, "Z", 9, 2, "Z", 8, 9],
          [6, 6, 8, 8, "Z", "Z", "Z", "Z", 7, 8],
          [7, 7, 7, 5, "Z", 8, 7, 8, 7, 9]]


class Node:
    def __init__(self, position, g, parent):
        self.position = position
        self.g = g + parent.g if parent is not None else g
        self.parent = parent

    def __str__(self):
        if self.parent is None:
            return f"([{self.position[1]},{self.position[0]}],{self.g},NULL)"
        else:
            return f"([{self.position[1]},{self.position[0]}],{self.g},[{self.parent.position[1]},{self.parent.position[0]}])"

    def __eq__(self, other):
        return self.position == other.position


def get_neighbors(node):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    neighbors = []
    for direction in directions:
        new_position = (node.position[0] + direction[0], node.position[1] + direction[1])
        if 0 <= new_position[0] < len(matrix[0]) and 0 <= new_position[1] < len(matrix) and \
                matrix[new_position[0]][new_position[1]] != "Z":
            neighbors.append(Node(new_position, matrix[new_position[0]][new_position[1]], node))
    return neighbors


def ucs_w_close():
    open_nodes = []
    closed_nodes = []

    # exchange the x and y coordinates of the start and end nodes that are given in the assignment
    start_node = Node((4, 3), 0, None)  # enter your start node here
    end_node = (7, 6)                   # enter your end node here

    open_nodes.append(start_node)

    i = -1

    while open_nodes:
        i += 1
        print(f"\nIteration:{i}")
        print("Open: \n", end="")
        print(','.join(str(node) for node in open_nodes))
        print("Closed: \n", end="")
        print(','.join(str(node) for node in closed_nodes))

        current_node = min(open_nodes, key=lambda x: x.g)
        open_nodes.remove(current_node)
        if current_node.position == end_node:
            print("Path found!")
            path = []
            while current_node is not None:
                path.append(str(current_node))
                current_node = current_node.parent
            print(" -> ".join(reversed(path)))
            return

        neighbors = get_neighbors(current_node)
        for neighbor in neighbors:
            if neighbor.position in [node.position for node in closed_nodes]:
                continue

            if neighbor not in open_nodes:
                open_nodes.append(neighbor)
            else:
                existing_node = open_nodes[open_nodes.index(neighbor)]
                if existing_node.g > neighbor.g:
                    open_nodes.remove(existing_node)
                    open_nodes.append(neighbor)

        closed_nodes.append(current_node)


if __name__ == '__main__':
    ucs_w_close()