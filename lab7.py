#depth Limited Search
'''class Tree:
    def _init_(self):  # Correction: double underscores
        self.tree = {}

    def add_edge(self, parent, child):
        if parent not in self.tree:
            self.tree[parent] = []
        if child not in self.tree:
            self.tree[child] = []
        self.tree[parent].append(child)

    def DLS(self, node, goal, limit, visited=None):
        if visited is None:
            visited = set()

        print(node, end=" ")

        if node == goal:
            print("\nGoal node found!")
            return True

        if limit <= 0:
            return False

        visited.add(node)
        for child in self.tree[node]:
            if child not in visited:
                if self.DLS(child, goal, limit - 1, visited):
                    return True

        return False

# Create the tree
tree = Tree()
tree.add_edge('A', 'B')
tree.add_edge('A', 'F')
tree.add_edge('A', 'D')
tree.add_edge('A', 'E')
tree.add_edge('B', 'K')
tree.add_edge('B', 'J')
tree.add_edge('K', 'N')
tree.add_edge('K', 'M')
tree.add_edge('D', 'G')
tree.add_edge('E', 'C')
tree.add_edge('E', 'H')
tree.add_edge('E', 'I')
tree.add_edge('I', 'L')

# Run Depth Limited Search
start_node = 'A'
goal_node = 'L'
depth_limit = 3

print(f"\nDLS from {start_node} to find {goal_node} with depth limit = {depth_limit}:")
found = tree.DLS(start_node, goal_node, depth_limit)

if not found:
    print("\nGoal node NOT found within the depth limit.")'''
    #iterative deepning Search
# Depth Limited Search with Iterative Deepening
class Tree:
    def _init_(self):  # Constructor
        self.tree = {}

    def add_edge(self, parent, child):
        if parent not in self.tree:
            self.tree[parent] = []
        if child not in self.tree:
            self.tree[child] = []
        self.tree[parent].append(child)

    def DLS(self, node, goal, limit, visited=None):
        if visited is None:
            visited = set()

        print(node, end=" ")

        if node == goal:
            print("\nGoal node found!")
            return True

        if limit <= 0:
            return False

        visited.add(node)
        for child in self.tree[node]:
            if child not in visited:
                if self.DLS(child, goal, limit - 1, visited):
                    return True

        return False

    def IDDFS(self, start, goal, max_depth):
        for depth in range(max_depth + 1):
            print(f"\nTrying depth limit: {depth}")
            if self.DLS(start, goal, depth):
                return True
        print("\nGoal node NOT found within maximum depth limit.")
        return False

# Create the tree
tree = Tree()
tree.add_edge('A', 'B')
tree.add_edge('A', 'F')
tree.add_edge('A', 'D')
tree.add_edge('A', 'E')
tree.add_edge('B', 'K')
tree.add_edge('B', 'J')
tree.add_edge('K', 'N')
tree.add_edge('K', 'M')
tree.add_edge('D', 'G') 
tree.add_edge('E', 'C')
tree.add_edge('E', 'H')
tree.add_edge('E', 'I')
tree.add_edge('I', 'L')

# Run Iterative Deepening Search
start_node = 'A'
goal_node = 'L'
max_depth = 5

print(f"\nIDDFS from {start_node} to find {goal_node} (max depth = {max_depth}):")
found = tree.IDDFS(start_node, goal_node, max_depth)

if not found:
    print("\nGoal node NOT found.")