class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for char in word:
          if char not in cur.children:
            cur.children[char] = TrieNode()
          cur = cur.children[char]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for char in word:
          if char not in cur.children:
            return False
          cur = cur.children[char]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
      cur = self.root

      for char in prefix:
        if char not in cur.children:
          return False
        cur = cur.children[char]
      return True
        
# Time insert - O(1) startsWith - O(1)

# Space O(N) - not sure, will update if wrong