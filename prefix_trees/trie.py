class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end_of_word = False  # Flag to mark end of a word
        self.count = 0  # Count of words that pass through this node


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.total_words = 0  # Counter for unique words

    def insert(self, word):
        """
        Insert a word into the trie
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1

        # Only increment total_words if this is a new word
        if not node.is_end_of_word:
            self.total_words += 1
        node.is_end_of_word = True

    def search(self, word):
        """
        Search for a word in the trie
        Returns True if the word exists, False otherwise
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        """
        Check if any word in the trie starts with the given prefix
        Returns True if prefix exists, False otherwise
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def get_words_with_prefix(self, prefix):
        """
        Get all words in the trie that start with the given prefix
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        words = []
        self._get_all_words_from_node(node, prefix, words)
        return words

    def _get_all_words_from_node(self, node, prefix, words):
        """
        Helper method to recursively get all words from a node
        """
        if node.is_end_of_word:
            words.append(prefix)

        for char, child_node in node.children.items():
            self._get_all_words_from_node(child_node, prefix + char, words)

    def count(self):
        """
        Get the total number of unique words in the trie.
        """
        return self.total_words

    def get_size(self):
        """
        Get the total number of words in the trie
        """
        return self.total_words
