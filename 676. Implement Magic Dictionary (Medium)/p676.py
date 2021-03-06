class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def buildDict(self, dictionary: List[str]) -> None:
        self.arr += dictionary
        

    def search(self, searchWord: str) -> bool:
        arr = [x for x in self.arr if len(x) == len(searchWord)]
        for w in arr:
            mismatch = 0
            for k, _ in enumerate(searchWord):
                if w[k] != searchWord[k]:
                    mismatch += 1
                    if mismatch > 1:
                        break
            if mismatch == 1:
                return True
        return False

        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)