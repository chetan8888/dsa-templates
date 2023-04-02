class Trie:
    def __init__(self):
        self.t = {}

    def insert(self,word):
        t = self.t
        for letter in word:
            if letter not in t:
                t[letter] = {}
            t = t[letter]
        t['#'] = '#'

    def search(self,word):
        t = self.t
        for letter in word:
            if letter not in t:
                return False
            t = t[letter]
        if '#' not in t:
            return False
        return True

    def startswith(self,prefix):
        t = self.t
        for letter in prefix:
            if letter not in t:
                return False
            t = t[letter]
        return True

a = ['oa','oaa','ab']
trie = Trie()
for word in a:
    trie.insert(word)
print(trie.startswith("o"))