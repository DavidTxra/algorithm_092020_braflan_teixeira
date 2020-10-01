import math

class FibonacciTree:
    def __init__(self, value):
        self.value = value
        self.child = []
        self.order = 0
        self.parent = None

    # ajouter l'arbre a la fin
    def add_tree(self, tree):
        self.child.append(tree)
        self.order = self.order + 1    


class FibonacciHeap:
    def __init__(self):
        self.trees = []
        self.least = None
        self.head = None
        self.count = 0

    # Ajoute une valeur dans l'arbre
    def insert(self, value):
        new_tree = FibonacciTree(value)
        self.trees.append(new_tree)
        if (self.least is None or value < self.least.value):
            self.least = new_tree 
        if (self.head is None or value > self.head.value):
            self.head = new_tree        
        self.count = self.count + 1

    # Retourne la valeur minimum dans l'arbre
    def find_min(self):
        if self.least is None:
            return None
        return self.least.value 

    # Retourne la valeur maximum dans l'arbre
    def find_max(self):
        if self.head is None:
            return None
        return self.head.value 

    def consolidate(self):
        aux = (floor(self.count) + 1) * [None]

        while self.trees != []:
            x = self.trees[0]
            order = x.order
            self.trees.remove(x)
            while aux[order] is not None:
                y = aux[order]
                if x.value > y.value:
                    x, y = y, x
                x.add_tree(y)
                aux[order] = None
                order = order + 1
            aux[order] = x

        self.least = None
        for k in aux:
            if k is not None:
                self.trees.append(k)
                if self.least is None or k.value < self.least.value:
                    self.least = k

def floor(x):
    return math.frexp(x)[1] - 1

fibonacci_heap = FibonacciHeap()

fibonacci_heap.insert(7)
fibonacci_heap.insert(3)
fibonacci_heap.insert(17)
fibonacci_heap.insert(24)
fibonacci_heap.insert(12)
fibonacci_heap.insert(3)
fibonacci_heap.insert(4)

print('Valeur minimum: ' + format(fibonacci_heap.find_min()))

print('Valeur maximum: ' + format(fibonacci_heap.find_max()))