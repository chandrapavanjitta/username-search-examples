class BPlusTreeNode:
    def __init__(self, is_leaf=False):
        self.is_leaf = is_leaf
        self.keys = []
        self.children = []

class BPlusTree:
    def __init__(self, order):
        self.root = BPlusTreeNode(is_leaf=True)
        self.order = order

    def insert(self, key):
        root = self.root
        if len(root.keys) == (self.order - 1):
            new_root = BPlusTreeNode()
            new_root.children.append(self.root)
            self._split_child(new_root, 0, self.root)
            self.root = new_root
        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node, key):
        if node.is_leaf:
            node.keys.append(key)
            node.keys.sort()  # Ensure keys are sorted after insertion
        else:
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (self.order - 1):
                self._split_child(node, i, node.children[i])
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def _split_child(self, parent, index, child):
        new_child = BPlusTreeNode(is_leaf=child.is_leaf)
        mid_index = len(child.keys) // 2
        parent.keys.insert(index, child.keys[mid_index])
        parent.children.insert(index + 1, new_child)

        new_child.keys = child.keys[mid_index + 1:]
        child.keys = child.keys[:mid_index]

        if not child.is_leaf:
            new_child.children = child.children[mid_index + 1:]
            child.children = child.children[:mid_index + 1]

    def display(self, node=None, level=0):
        if node is None:
            node = self.root
        print("Level", level, ":", node.keys)
        if not node.is_leaf:
            for child in node.children:
                self.display(child, level + 1)  
    
    def count(self):
        """
        Count the total number of keys in the B+ tree by visiting all nodes.
        """
        def count_keys(node):
            if node.is_leaf:
                return len(node.keys)
            return len(node.keys) + sum(count_keys(child) for child in node.children)

        return count_keys(self.root)

    def search(self, key):
        """
        Search for a key in the B+ tree. Returns True if the key exists, otherwise False.
        """
        def search_node(node, key):
            if key in node.keys:
                return True

            if node.is_leaf:
                return False

            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            return search_node(node.children[i], key)

        return search_node(self.root, key)