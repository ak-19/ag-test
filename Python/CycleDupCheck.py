class CycleDupCheck:
    def __init__(self, graph, items) -> None:
        self.graph = graph
        self.items = items

    def raise_error_cycle_or_duplicate(self):
        visited = set()
        seen_on_this_path = set()
        def dfs(node):
            seen_on_this_path.add(node)
            visited.add(node)
            for to in self.graph[node]:
                if to not in visited: dfs(to)
                elif to in seen_on_this_path: raise Exception('Cycle detected')
            seen_on_this_path.remove(node)

        occurence = set()
        for item in self.items:
            name = item['name']
            if name in occurence: raise Exception('Items with duplicate names detected')
            occurence.add(name)
            if name not in visited: dfs(name)    