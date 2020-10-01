class FibonacciTree:
    def __init__(self, value):
        self.value = value
        self.child = []
        self.order = 0
        self.parent = None


class FibonacciHeap:
    def __init__(self):
        self.trees = []
        self.least = None
        self.count = 0

    # Ajoute une valeur dans l'arbre
    def insert(self, value):
        new_tree = FibonacciTree(value)
        self.trees.append(new_tree)
        if (self.least is None or value < self.least.value):
            self.least = new_tree
        self.count = self.count + 1

    # Retourne la valeur minimum dans l'arbre
    def find_min(self):
        if self.least is None:
            return None
        return self.least.value    



fibonacci_heap = FibonacciHeap()

fibonacci_heap.insert(7)
fibonacci_heap.insert(3)
fibonacci_heap.insert(17)
fibonacci_heap.insert(24)
fibonacci_heap.insert(1)
fibonacci_heap.insert(12)
fibonacci_heap.insert(3)
fibonacci_heap.insert(4)

print('Valeur minimum: ' + format(fibonacci_heap.find_min()))
