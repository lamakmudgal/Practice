class TrieNode:
    def __init__(self):
        self.children =[None]*26
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    # To convert char into index so we can store all character
    # in 26 lowercase string.
    def _getindex(self,char):
        return ord(char)-ord("a")

    def insertword(self,word):
        crawler = self.root
        for chars in word:
            index = self._getindex(chars)
            if not crawler.children[index]:
                crawler.children[index] = self.getNode()
            crawler = crawler.children[index]
        crawler.end_of_word = True
        print("added", word)

    def searchaword(self,word):
        searcher = self.root
        for chars in word:
            print("Searching for :",chars)
            index = self._getindex(chars)
            if not searcher.children[index]:
                print("Not Found")
                return False
            searcher = searcher.children[index]
        if searcher.end_of_word and searcher is not None:
            print("Found the word")

if __name__ == '__main__':
    keys = ["the", "a", "there", "answer", "any",
            "by", "their"]
    t = Trie()
    for key in keys:
        t.insertword(key)

    t.searchaword("their")

