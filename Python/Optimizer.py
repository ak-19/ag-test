from collections import defaultdict, Counter, deque
from CycleDupCheck import CycleDupCheck


class Optimizer:
    def __init__(self, items, total_space) -> None:
        self.items = items
        self.N = len(items)
        self.total_space = total_space
        self.graph = defaultdict(set)
        self.lookup = dict()
        for item in items:
            name = item["name"]
            for dep in item["dependencies"]:
                self.graph[dep].add(name)
            self.lookup[name] = item

        CycleDupCheck(self.graph, items).raise_error_cycle_or_duplicate()

        self.solution, self.solution_value = [], 0

    def get_optimized_data(self):
        self.optimize(self.get_toplogical_ordered_items())
        return self.solution

    def get_result(self):
        item_names = self.get_optimized_data()
        return {"total_value": self.solution_value, "items": list(map(lambda x: self.lookup[x], item_names))}

    def higher_priority(self, one, other):
        for a, b in zip(one, other):
            if self.lookup[a]["priority"] > self.lookup[b]["priority"]:
                return False
            if self.lookup[a]["priority"] < self.lookup[b]["priority"]:
                return True
        return False

    def try_to_update_solution(self, value, seen):
        if value > self.solution_value:
            self.solution_value = value
            self.solution = sorted(list(seen), key=lambda x: self.lookup[x]["priority"])
        elif value == self.solution_value:
            candidate = sorted(list(seen), key=lambda x: self.lookup[x]["priority"])
            if self.higher_priority(candidate, self.solution):
                self.solution = candidate

    def get_size(self, item_name):
        return self.lookup[item_name]["size"]

    def get_val(self, item_name):
        return self.lookup[item_name]["value"]

    def dependencies_met(self, item_name, seen):
        return all(dep in seen for dep in self.lookup[item_name]["dependencies"])

    def optimize(self, ordered_items):
        seen = set()

        def search(idx, space_left, value):
            if idx == self.N:
                self.try_to_update_solution(value, seen)
                return
            name = ordered_items[idx]
            if self.get_size(name) <= space_left:
                if self.dependencies_met(name, seen):
                    seen.add(name)
                    search( idx + 1, space_left - self.get_size(name), value + self.get_val(name))
                    seen.remove(name)
            search(idx + 1, space_left, value)

        search(0, self.total_space, 0)

    def get_toplogical_ordered_items(self):
        indeg = Counter()
        for node in self.lookup:
            for neighbor in self.graph[node]:
                indeg[neighbor] += 1
        qu = deque()
        for node in self.lookup:
            if indeg[node] == 0:
                qu.append(node)
        result = []
        while qu:
            node = qu.popleft()
            result.append(node)
            for nei in self.graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    qu.append(nei)
        return result
