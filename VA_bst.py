"""
Solutions to module VA bst

Student:
Mail:
"""
author = ''
reviewer = ''




class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Discussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)



    def ipl(self):
        return self._ipl(self.root,1)
    def _ipl(self, r, depth):
        if r is None:
            return 0
        return depth + self._ipl(r.left, depth+1) + self._ipl(r.right, depth+1)

    def height(self):
        return self._height(self.root)
    def _height(self, r):
        if r is None:
            return 0
        return 1 + max(self._height(r.left), self._height(r.right))

def random_tree(n):                               # Useful
    import random
    t = BST()
    for _ in range(n):
        t.insert(random.random())
    return t





def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print()


    for k in range(1, 10):
        import math
        n = 1000 * 2**k
        tree = random_tree(n)

        ipl = tree.ipl()
        height = tree.height()
        print(f"tree with n = {n} : IPL = {ipl}, Height = {height}, IPL/n = {ipl/n:.4f}",
              f"theory IPL/n = {1.39 * math.log2(n):.4f}")



if __name__ == "__main__":
    main()


"""

Results for ipl of random trees

tree with n = 2000 : IPL = 28701, Height = 28, IPL/n = 14.3505 theory IPL/n = 15.2424
tree with n = 4000 : IPL = 57321, Height = 26, IPL/n = 14.3302 theory IPL/n = 16.6324
tree with n = 8000 : IPL = 124631, Height = 29, IPL/n = 15.5789 theory IPL/n = 18.0224
tree with n = 16000 : IPL = 278774, Height = 31, IPL/n = 17.4234 theory IPL/n = 19.4124
tree with n = 32000 : IPL = 614574, Height = 34, IPL/n = 19.2054 theory IPL/n = 20.8024
tree with n = 64000 : IPL = 1243312, Height = 35, IPL/n = 19.4267 theory IPL/n = 22.1924
tree with n = 128000 : IPL = 2901299, Height = 42, IPL/n = 22.6664 theory IPL/n = 23.5824
tree with n = 256000 : IPL = 6191447, Height = 46, IPL/n = 24.1853 theory IPL/n = 24.9724
tree with n = 512000 : IPL = 12277091, Height = 50, IPL/n = 23.9787 theory IPL/n = 26.3624
===============================
How well does that agree with the theory?
The experiments show that the IPL/n ratio aligns well with the theoretical predictions as n increases, 
confirming that the theory provides an accurate model for large random binary search trees. 

What can you guess about the height?
The tree height remains relatively low compared to the number of nodes,
suggesting that the height grows logarithmically with n, as expected.
"""
