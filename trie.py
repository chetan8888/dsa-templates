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

    def deleteHelper(self,word,index,t):
        if len(word) == index:
            del t['#']
            return

        self.deleteHelper(word,index+1,t[word[index]])
        if len(t[word[index]].keys())==0:
            del t[word[index]]
    
    def deleteWord(self,word):
        if self.search(word):
            self.deleteHelper(word,0,self.t)
    
    


a = ['flower', 'fly', 'few', 'feww']
trie = Trie()
for word in a:
    trie.insert(word)
print(trie.t)
trie.deleteWord('few')
print(trie)